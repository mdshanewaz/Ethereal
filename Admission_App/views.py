from django.shortcuts import render

# Create your views here.

def admission_notice_view(request):
    title = 'Admission Notice | ETHEREAL'

    context = {
        'title' : title,
    }

    return render(request, 'Admission_App/admision.html', context=context)

def admission_process_view(request):
    title = 'Admission Process | ETHEREAL'

    context = {
        'title' : title,
    }

    return render(request, 'Admission_App/process.html', context=context)