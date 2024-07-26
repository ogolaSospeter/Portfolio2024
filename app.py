from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_mail import  Message, Mail
import sys, os
import configparser
from file import get_education_data, get_programming_languages_data, get_technical_skills_data, get_projects_data

config = configparser.ConfigParser()
config.read('config.ini')


app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = config.get('userdata','Email')
app.config['MAIL_PASSWORD'] = config.get('userdata','Password')

app.config['SECRET_KEY'] = config['userdata']['secretKey']

mail = Mail(app)




@app.route('/',methods=['GET','POST'])
def index():
    return render_template('main.html')

@app.route('/sendemail/', methods=['POST'])
def send_email():
    # Get form data
    name = request.form['name']
    subject = request.form['Subject']
    email = request.form['_replyto']
    message = request.form['message']
    try:
        sendemail(email,config['userdata']['Email'], config['userdata']['Password'], message, subject, name)
        flash('Message Sent', 'success')
        
    except Exception as e:
        flash('Message not sent', 'danger')
        print(e)
    return redirect(url_for('index'))


def prepare_mail(message, email,subject, name):
    msg = MIMEMultipart("alternative")
    msg["From"] = email
    msg["To"] = config.get("userdata", "Email")
    msg["Subject"] = subject
    
    html = f"<p>{message}</p>"
    text_part = MIMEText(message, "plain")
    html_part = MIMEText(html, "html")
    msg.attach(text_part)
    msg.attach(html_part)
    return msg.as_string()

def sendemail(senderemail,email, password, message, subject,name,verbose=1):
    server = smtplib.SMTP(host="smtp.office365.com", port=587)
    server.starttls()
    server.login(email, password)
    server.sendmail(senderemail, email,prepare_mail(message,email,subject, name))
    server.quit()
    if verbose:
        flash('Message Sent', 'success'),200
        # print(f"{datetime.now()} - Sent an email to {email}  from {senderemail}  with subject {subject}")



#Create an education details API for my portfolio
@app.route('/education/')

def educationData():
    data =  get_education_data()
    return jsonify(data)
    
@app.route('/programminglanguages')
def programLang():
    langData = get_programming_languages_data()
    return jsonify(langData)


@app.route('/technicalskills')
def frameworks():
    frameData = get_technical_skills_data()
    return jsonify(frameData)

@app.route('/projects')
def projectsViews():
    projectsData = get_projects_data()
    return jsonify(projectsData)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105,debug=True)