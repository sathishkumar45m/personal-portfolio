from django.shortcuts import render
from django import forms
from .forms import Contactformemail
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request, 'home.html')
def skills(request):
    skills_list = [
        {"name": "Python"},
        {"name": "Django"},
        {"name": "JavaScript"},
        {"name": "Linux"},
        {"name": "HTML"},
        {"name":"CSS"},
        {"name":"PROBLEM SOLVER"},
        {"name":"CREATIVE THINKER"}
    ]
    return render(request, 'skills.html', {"skills": skills_list})

def about(request):
    return render(request, 'about.html')




def projects(request):
    project_list = [
        {
            'title': 'Portfolio Website',
            'description': 'A personal portfolio website built with Django, web technologies, and SQLite.',
            'techs': ['HTML', 'CSS', 'JavaScript', 'Python', 'Django', 'SQLite']
        },
        {
            'title': 'E-commerce Platform',
            'description': 'A food order e-commerce platform with user authentication.',
            'techs': ['HTML', 'CSS', 'JavaScript', 'Python', 'Django', 'SQLite']
        },
        {
            'title': 'Calculator',
            'description': 'A real-time calculator built using HTML, CSS, and JavaScript.',
            'techs': ['HTML', 'CSS', 'JavaScript']
        },
    ]
    return render(request, 'projects.html', {'projects': project_list})




def contact(request):
    if request.method == 'GET':
        form = Contactformemail()
    else:
        form = Contactformemail(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Construct email body with name
            full_message = f"From: {name} <{from_email}>\n\n{message}"
            
            # Sending email
            send_mail(
                subject,
                full_message,
                from_email,
                ['sathishkumar07610761@gmail.com', from_email],
                fail_silently=False
            )
    
    return render(request, 'contact.html', {'form': form})
