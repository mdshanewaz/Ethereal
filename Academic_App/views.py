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

def bookList_view(request):
    title = 'Book List | EHEREAL'

    context = {
        'title' : title,
    }

    return render(request, 'Academic_App/book_list.html', context=context)

def classSchedule_view(request):
    title = 'Class Schedule | EHEREAL'

    context = {
        'title' : title,
    }

    return render(request, 'Academic_App/class_schedule.html', context=context)

def examSchedule_view(request):
    title = 'Exam Schedule | EHEREAL'

    context = {
        'title' : title,
    }

    return render(request, 'Academic_App/exam_schedule.html', context=context)