from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


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
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "You Were Logged Out")
    return redirect('home')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
        return redirect('home')
    else:
        form = UserCreationForm()
    context = {
        "title": "Register",
        "form": form
    }
    return render(request, "authenticate/register.html", context)
