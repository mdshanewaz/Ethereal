from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from academic_app.forms import *

# Create your views here.

def curriculum_view(request):
    title = 'Curriculum | ETHEREAL'

    context = {
        'title' : title,
    }

    return render(request, 'academic_app/currucullum.html', context=context)

def syllabus_view(request):
    title = 'Syllabus | ETHEREAL'

    context = {
        'title' : title,
    }

    return render(request, 'academic_app/syllabus.html', context=context)

def bookList_view(request):
    title = 'Book List | ETHEREAL'

    context = {
        'title' : title,
    }

    return render(request, 'academic_app/book_list.html', context=context)

def classSchedule_view(request):
    title = 'Class Schedule | ETHEREAL'

    context = {
        'title' : title,
    }

    return render(request, 'academic_app/class_schedule.html', context=context)

def examSchedule_view(request):
    title = 'Exam Schedule | ETHEREAL'

    context = {
        'title' : title,
    }

    return render(request, 'academic_app/exam_schedule.html', context=context)

def career_view(request):
    title = 'Career | ETHEREAL'

    if request.method == 'POST':
        personal_form = PersonalForm(request.POST, request.FILES)

        education_formset = EducationFormSet(request.POST, instance=personal_form.instance)
        training_formset = TrainingFormSet(request.POST, instance=personal_form.instance)
        experience_formset = ExperienceFormSet(request.POST, instance=personal_form.instance)
        skill_formset = SkillFormSet(request.POST, instance=personal_form.instance)
        reference_formset = ReferenceFormSet(request.POST, instance=personal_form.instance)

        if (personal_form.is_valid() and education_formset.is_valid() and training_formset.is_valid() and experience_formset.is_valid() and skill_formset.is_valid() and reference_formset.is_valid()):

            personal_instance = personal_form.save()

            education_formset.instance = personal_instance
            education_formset.save()
            training_formset.instance = personal_instance
            training_formset.save()
            experience_formset.instance = personal_instance
            experience_formset.save()
            skill_formset.instance = personal_instance
            skill_formset.save()
            reference_formset.instance = personal_instance
            reference_formset.save()

            subject = f"Career mail from {personal_instance.name}"
            message = f"Name: {personal_instance.name} has submitted an appliaction for starting career at your school. Please visit the Admin Panel for details."

            send_mail(subject, message, settings.EMAIL_HOST_USER, ["career.ethereal@gmail.com"])


            return redirect('academic_app:thank_you')

    else:
        personal_form = PersonalForm()
        education_formset = EducationFormSet()
        training_formset = TrainingFormSet()
        experience_formset = ExperienceFormSet()
        skill_formset = SkillFormSet()
        reference_formset = ReferenceFormSet()

    context = {
        'title' : title,
        'personal_form': personal_form,
        'education_formset': education_formset,
        'training_formset': training_formset,
        'experience_formset': experience_formset,
        'skill_formset': skill_formset,
        'reference_formset': reference_formset
    }

    return render(request, 'academic_app/career.html', context=context)

def thank_you_view(request):
    title = 'Thank You | ETHEREAL'

    context = {
        'title' : title,
    }
    return render(request, 'academic_app/thank_you.html',  context=context)

def year_planner_view(request):
    title = 'Year Planner | ETHEREAL'

    context = {
        'title' : title,
    }
    return render(request, 'academic_app/year_planner.html',  context=context)