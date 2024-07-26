from datetime import datetime
import json


def serialize(obj):
    if isinstance(obj, bytes):
        return obj.decode('utf-8')
    raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')

def create_json_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, default=serialize, indent=4)


def read_data_from_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def write_data_to_file(new_data, filename):
    existing_data = read_data_from_file(filename)
    existing_data.append(new_data)
    with open(filename, 'w') as file:
        json.dump(existing_data, file)

def add_project_to_data(new_project):
    data = read_data_from_file('profile_data.json')
    data['projects'].append(new_project)
    create_json_file(data, 'profile_data.json')


def get_education_data():
    data = read_data_from_file('profile_data.json')
    return data.get('education', [])

def get_programming_languages_data():
    data = read_data_from_file('profile_data.json')
    return data.get('programming_languages', [])

def get_technical_skills_data():
    data = read_data_from_file('profile_data.json')
    return data.get('technicalskills', [])

def get_projects_data():
    data = read_data_from_file('profile_data.json')
    return sorted(data.get('projects', []), key=lambda x: extract_year(x['year']), reverse=True)

def extract_year(date_str):
    # Parse the date string into a datetime object
    date_obj = datetime.strptime(date_str, "%B, %Y")
    # Extract and return the year
    return date_obj.year


data = {
    "education": [
{
    'levelTitle': "Bachelor's Computer Technology",
    'institution': 'JOMO KENYATTA UNIVERSITY of AGRICULTURE and TECHNOLOGY.',
    'year': '2021 - Current',
    'projects': [
        {'name': 'In-Person Service Finder', 'description': 'ALX-SE Team Project'},
        {'name': 'Customizable Recipe Website', 'description': 'ALX-SE Solo Project'},
    ]
},
    {
        'levelTitle': "Kenya Certificate of Secondary Education",
        'institution': 'HomaBay High School',
        'year': '2016 - 2019',
        'projects': [
            {'name': 'School Voting System', 'description': 'KCSE Project'}
        ]
    },
    {
        'levelTitle': "Kenya Certificate of Primary Education",
        'institution': 'Ogande Junior Academy',
        'year': '2008 - 2015',
        'projects': [
            {'name': '', 'description': ''}
        ]
    },
    {
        'levelTitle': "Other Certifications",
        'institution': 'ALX Africa',
        'year': '2020 - Current',
        'projects': [
            {'name': 'ALX Africa', 'description': 'ALX Africa'},
        ]
    },
    {
        'levelTitle': "Other Certifications",
        'institution': 'Microsoft Learn',
        'year': 'May - July,2023',
        'projects': [
            {'name': 'Microsoft Learn', 'description': 'Microsoft Learn'},
        ]
    }
],
"programming_languages":[
    
    {
        'name': 'HTML',
        'title': 'Frontend Development of my Website Projects',
        'description': 'Used in my projects for the frontend development/ the Graphical User Interface..',
        'image': 'https://www.w3.org/html/logo/downloads/HTML5_Logo_512.png',
        'level': 'Intermediate'
    },
    {
        'name': 'CSS',
        'title': 'Styling of my Website Projects',
        'description': 'Has played a major role in the styling of my website projects..',
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSIB8xYDdx2TWL5IkMRT8zPQZV12Pqi_t_eUKzjjg1CsA&s',
        'level': 'Intermediate'
    },
    {
        'name': 'Kotlin',
        'title': 'Android Applications Development Language',
        'description': 'Kotlin is a cross-platform, statically typed, general-purpose programming language with type inference, mostly used for android Applicationsdevelopment..',
        'image': 'data:image/jpeg;base64,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',
        'level': 'Intermediate'
    },
        {
        'name': 'Python',
        'title': 'Backend Development[Routing, API management] of my Website Projects',
        'description': 'Python has allowed me to work quickly and integrate systems more effectively, thus a fast realization of my projects..',
        'image': 'https://www.python.org/static/community_logos/python-logo-master-v3-TM.png',
        'level': 'Intermediate'
    },
    {
        'name': 'JavaScript',
        'title': 'Backend Development and Interactivity of my Website Projects',
        'description': 'I have used JavaScript to add to the  interactivity of my website projects..',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/JavaScript-logo.png/600px-JavaScript-logo.png',
        'level': 'Intermediate'

    },
    {
        'name': 'SQL',
        'description': 'In my recently worked projects, I have used SQL to store, retrieve and manipulate the database records..',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Postgresql_elephant.svg/512px-Postgresql_elephant.svg.png',
        'level': 'Intermediate'
    }
], 
"technicalskills": [
    {
        'name':'Tools',
        'decs': [
            {'name':'NumPy'},
            {'name':'MS Excel'}
        ]
    },
    {
        'name':'Database Management Systems',
        'decs': [
            {'name':'MySQL'},
            {'name':'SQLite3'}
        ]
    },
    {
        'name':'Internet Technologies',
        'decs': [
            {'name':'Flask'},
            {'name':'HTML5'},
            {'name':'CSS'},
            {'name':'Bootstrap'}
        ]
    },
    {
        'name': 'Android App Development',
        'decs': [
            {'name':'Kotlin'},
            {'name':'Android Studio'}
        ]
    },
    {
        'name': 'Version Control',
        'decs': [
            {'name':'Git'},
            {'name':'GitHub'}
        ]
    },
    
],
"projects":[
    {
        'name': 'JKUSA Election Voting System',
        'description': 'As an academic project during the 3.1 Semester, in a team of 5, we developed an election system that would help aleviate the problems around the elections.',
        'image': 'https://img.freepik.com/free-vector/internet-electronic-voting_74855-4428.jpg?w=740&t=st=1707500917~exp=1707501517~hmac=1dc9ae930fd1d183fcaafba76a6629ebfa86aa1aae879e5f09c36ec5ba4f65b2',
        'image1':'/static/images/adminReview.jpg',
        'link': 'https://github.com/ogolaSospeter/CampusVoterSystem',
        'year':'November, 2023'
    },
    {
        'name': 'In-Person Service Finder',
        'description': 'Developed a platform that would allow users to find serice providers within their locality, allowing users to rate the services they receive from the service providers, thus aleviating the hustle of moving around seeking for a service provider. ',                
        'image': 'https://github.com/gims-inc/IPSP/blob/master/web_dynamic/static/images/on_phone2.jpeg?raw=true',
        'image1':'/static/images/adminReview.jpg',            
        'link': 'https://github.com/gims-inc/IPSP',
        'year':'May, 2023'
    },
    {
        'name': 'Customizable Recipe Website',
        'description': 'This is a web application that allows users to find recipes for their favorite meals. The application also allows users to add their own recipes.',
        'image': '/static/images/adminReview.jpg',
        'image1':'/static/images/main.jpg',
        'link': 'https://github.com/ogolaSospeter/WebstackPortfolioProject',
        'year':'June, 2023'
    },
    {
        'name':'Skyliners Boutique Parlor',
        'description':'After weeks of self-paced learning, I developed this android project that is an e-commerce site specifically for selling clothewear and the footwear.',
        'image':'https://github.com/ogolaSospeter/SkylineBoutiqueApp/raw/master/Skyline%20Boutique/images/logo.png',
        'image1':'https://github.com/ogolaSospeter/SkylineBoutiqueApp/raw/master/Skyline%20Boutique/images/home.png',
        'image2':'https://github.com/ogolaSospeter/SkylineBoutiqueApp/raw/master/Skyline%20Boutique/images/logsuccess.png',
        'link':'https://github.com/ogolaSospeter/SkylineBoutiqueApp/tree/master',
        'year':'March, 2023'

    }
]
}


# create_json_file(data, 'profile_data.json')

new_project = {
    'name': 'NAO Robot Teaching Assistant',
    'description': 'Currently working on a project that will see the development of a robot that will be used to assist in teaching of the students in the university.',
    'image' : 'https://www.aldebaran.com/sites/default/files/2018-06/nao-robot_0.jpg',
    'image1': '/static/images/adminReview.jpg',
    'link': 'https://github.com/ogolaSospeter/NAORobotTeachingAssistant',
    'year': 'February, 2024'
}

# add_project_to_data(new_project)