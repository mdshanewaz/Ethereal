from django.shortcuts import render, HttpResponse, redirect
from Academic_App.forms import *

# Create your views here.

def curriculum_view(request):
    title = 'Curriculum | ETHEREAL'

    context = {
        'title' : title,
    }

    return render(request, 'Academic_App/currucullum.html', context=context)

def syllabus_view(request):
    title = 'Syllabus | ETHEREAL'

    context = {
        'title' : title,
    }

    return render(request, 'Academic_App/syllabus.html', context=context)

def bookList_view(request):
    title = 'Book List | ETHEREAL'

    context = {
        'title' : title,
    }

    return render(request, 'Academic_App/book_list.html', context=context)

def classSchedule_view(request):
    title = 'Class Schedule | ETHEREAL'

    context = {
        'title' : title,
    }

    return render(request, 'Academic_App/class_schedule.html', context=context)

def examSchedule_view(request):
    title = 'Exam Schedule | ETHEREAL'

    context = {
        'title' : title,
    }

    return render(request, 'Academic_App/exam_schedule.html', context=context)

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

            return redirect('Academic_App:thank_you')

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

    return render(request, 'Academic_App/career.html', context=context)

def thank_you_view(request):
    title = 'Thank You | ETHEREAL'

    context = {
        'title' : title,
    }
    return render(request, 'Academic_App/thank_you.html',  context=context)
