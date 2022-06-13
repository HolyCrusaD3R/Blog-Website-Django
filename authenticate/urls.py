from django.urls import path
from . import views

urlpatterns = [
    path('log-in/', views.logIn, name="log-in"),
    path('log-out/', views.logOut, name="log-out"),
]
