from django.shortcuts import render, HttpResponse

# Create your views here.

def about_view(request):
    title = 'EHEREAL an English Medium School'

    context = {
        'title' : title,
    }

    return render(request, 'About_App/about.html', context=context)
