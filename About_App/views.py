from django.shortcuts import render, HttpResponse
from About_App.models import FacultyModel

# Create your views here.

def home_view(request):
    title = 'ETHEREAL An English Medium School'

    context = {
        'title' : title,
    }

    return render(request, 'About_App/home.html', context=context)


def about_view(request):
    title = 'About | Ethereal'

    context = {
        'title' : title,
    }

    return render(request, 'About_App/about.html', context=context)

def feature_view(request):
    title = 'Feature | Ethereal'

    context = {
        'title' : title,
    }

    return render(request, 'About_App/feature.html', context=context)

def teacher_view(request):
    title = 'Faculty | Ethereal'
    faculty_members = FacultyModel.objects.all()

    context = {
        'title' : title,
        'faculty_members' : faculty_members,
    }

    return render(request, 'About_App/teachers.html', context=context)

def extracurr_view(request):
    title = 'Exttracurricular | Ethereal'

    context = {
        'title' : title,
    }

    return render(request, 'About_App/extracurricular.html', context=context)

def resourceful_campus_view(request):
    title = 'Resourceful Campus | Ethereal'

    context = {
        'title' : title,
    }

    return render(request, 'About_App/resourcefull_campus.html', context=context)

def hifz_view(request):
    title = 'Hifz | Ethereal'

    context = {
        'title' : title,
    }

    return render(request, 'About_App/hifz.html', context=context)

def contact_view(request):
    title = 'Contact | ETHEREAL'

    context = {
        'title' : title,
    }

    return render(request, 'About_App/contact.html', context=context)