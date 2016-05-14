from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.views.generic import FormView

from .foms import LoginForm


class LoginView(FormView):

    form_class = LoginForm

    return render(request, 'login.html')


def Logout(request):
    logout(request)
    return redirect('/')
