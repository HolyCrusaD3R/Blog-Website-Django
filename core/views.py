from django.shortcuts import render


def home(request):
    context = {
        'title': 'Home Page'
    }
    return render(request, 'core/home.html', context)
