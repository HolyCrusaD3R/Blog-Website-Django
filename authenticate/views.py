from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def logIn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, "There Was An Error. Try Again...")
            return redirect('log-in')
    else:
        context = {
            "title": "Log In"
        }
        return render(request, 'authenticate/log-in.html', context)


def logOut(request):
    logout(request)
    messages.success(request, "You Were Logged Out")
    return redirect('home')
