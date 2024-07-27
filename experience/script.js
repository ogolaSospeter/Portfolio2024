$(document).ready(function() {

    $('#menu').click(function() {
        $(this).toggleClass('fa-times');
        $('.navbar').toggleClass('nav-toggle');
    });

    $(window).on('scroll load', function() {
        $('#menu').removeClass('fa-times');
        $('.navbar').removeClass('nav-toggle');

        if (window.scrollY > 60) {
            document.querySelector('#scroll-top').classList.add('active');
        } else {
            document.querySelector('#scroll-top').classList.remove('active');
        }
    });
});

/* ===== SCROLL REVEAL ANIMATION ===== */
const srtop = ScrollReveal({
    origin: 'top',
    distance: '80px',
    duration: 1000,
    reset: true
});

/* SCROLL EXPERIENCE */
srtop.reveal('.experience .timeline', { delay: 400 });
srtop.reveal('.experience .timeline .container', { interval: 400 });


// Start of Tawk.to Live Chat
var Tawk_API = Tawk_API || {},
    Tawk_LoadStart = new Date();
(function() {
    var s1 = document.createElement("script"),
        s0 = document.getElementsByTagName("script")[0];
    s1.async = true;
    s1.src = 'https://embed.tawk.to/60df10bf7f4b000ac03ab6a8/1f9jlirg6';
    s1.charset = 'UTF-8';
    s1.setAttribute('crossorigin', '*');
    s0.parentNode.insertBefore(s1, s0);
})();
// End of Tawk.to Live Chat


// disable developer mode
document.onkeydown = function(e) {
    if (e.keyCode == 123) {
        return false;
    }
    if (e.ctrlKey && e.shiftKey && e.keyCode == 'I'.charCodeAt(0)) {
        return false;
    }
    if (e.ctrlKey && e.shiftKey && e.keyCode == 'C'.charCodeAt(0)) {
        return false;
    }
    if (e.ctrlKey && e.shiftKey && e.keyCode == 'J'.charCodeAt(0)) {
        return false;
    }
    if (e.ctrlKey && e.keyCode == 'U'.charCodeAt(0)) {
        return false;
    }
}

document.addEventListener('visibilitychange',
    function() {
        if (document.visibilityState === "visible") {
            document.title = "Experience | Portfolio Ogola Sospeter";
            $("#favicon").attr("href", "/assets/images/favicon.png");
        } else {
            document.title = "Come Back To Portfolio";
            $("#favicon").attr("href", "/assets/images/favhand.png");
        }
    });


document.addEventListener('DOMContentLoaded', function() {
    fetch('./experiences.json')
        .then(response => response.json())
        .then(data => {
            const timeline = document.getElementById('experience-timeline');
            let isRight = true;

            data.forEach(experience => {
                const containerDiv = document.createElement('div');
                containerDiv.className = `container ${isRight ? 'right' : 'left'}`;

                const contentDiv = document.createElement('div');
                contentDiv.className = 'content';

                const tagDiv = document.createElement('div');
                tagDiv.className = 'tag';
                const h2 = document.createElement('h2');
                h2.textContent = experience.company;
                tagDiv.appendChild(h2);

                const descDiv = document.createElement('div');
                descDiv.className = 'desc';
                const h3 = document.createElement('h3');
                h3.textContent = experience.role;
                const p = document.createElement('p');
                p.textContent = experience.duration;
                descDiv.appendChild(h3);
                descDiv.appendChild(p);

                contentDiv.appendChild(tagDiv);
                contentDiv.appendChild(descDiv);
                containerDiv.appendChild(contentDiv);

                timeline.appendChild(containerDiv);

                isRight = !isRight;
            });
        })
        .catch(error => console.error('Error fetching experience data:', error));
});