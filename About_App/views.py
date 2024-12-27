from django.shortcuts import render, HttpResponse

# Create your views here.

def home_view(request):
    title = 'EHEREAL An English Medium School'

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