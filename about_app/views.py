from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from about_app.models import FacultyModel, ContactModel
from about_app.forms import ContactForm


# Create your views here.

def home_view(request):
    title = 'ETHEREAL An English Medium School'

    context = {
        'title' : title,
    }

    return render(request, 'about_app/home.html', context=context)

def about_view(request):
    title = 'About | Ethereal'

    context = {
        'title' : title,
    }

    return render(request, 'about_app/about.html', context=context)

def feature_view(request):
    title = 'Feature | Ethereal'

    context = {
        'title' : title,
    }

    return render(request, 'about_app/feature.html', context=context)

def teacher_view(request):
    title = 'Faculty | Ethereal'
    faculty_members = FacultyModel.objects.all()

    context = {
        'title' : title,
        'faculty_members' : faculty_members,
    }

    return render(request, 'about_app/teachers.html', context=context)

def extracurr_view(request):
    title = 'Exttracurricular | Ethereal'

    context = {
        'title' : title,
    }

    return render(request, 'about_app/extracurricular.html', context=context)

def resourceful_campus_view(request):
    title = 'Resourceful Campus | Ethereal'

    context = {
        'title' : title,
    }

    return render(request, 'about_app/resourcefull_campus.html', context=context)

def hifz_view(request):
    title = 'Hifz | Ethereal'

    context = {
        'title' : title,
    }

    return render(request, 'about_app/hifz.html', context=context)

def contact_view(request):
    title = 'Contact | ETHEREAL'
    form = ContactForm

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            apply = form.save()

            subject = f"Contact mail from {apply.name}"
            message = f"Name: {apply.name}\nEmail: {apply.email}\nPhone Number: {apply.phone}\nGrade: {apply.grade}\nMessage: {apply.message}"

            send_mail(subject, message, settings.EMAIL_HOST_USER, ["ethereal.edu.bd@gmail.com"])

            return HttpResponseRedirect(reverse('about_app:thanks'))

    context = {
        'title' : title,
        'form' : form,
    }

    return render(request, 'about_app/contact.html', context=context)

def thanks_view(request):
    title = 'Thank You Contact | ETHEREAL'

    context = {
        'title' : title,
    }

    return render(request, 'about_app/thank_you.html', context=context)