from django.shortcuts import render, HttpResponse

# Create your views here.

def curriculum_view(request):
    title = 'Curriculum | EHEREAL'

    context = {
        'title' : title,
    }

    return render(request, 'Academic_App/currucullum.html', context=context)

def syllabus_view(request):
    title = 'Syllabus | EHEREAL'

    context = {
        'title' : title,
    }

    return render(request, 'Academic_App/syllabus.html', context=context)