from django.shortcuts import render, HttpResponse

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

    context = {
        'title' : title,
    }

    return render(request, 'Academic_App/career.html', context=context)
