from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login

from .foms import LoginForm


def login_view(request):

    if request.user.is_athenticated():

        redirect('/')

    elif request.POST:

        login_form = LoginForm(request.POST)

        if login_form.is_valid:

            user = authenticate(username=login_form.cleaned_data['username'],
                                password=login_form.cleaned_data['password'])

            if user is not None:
                login(user)
                return redirect('/')
            else:
                login_form = LoginForm()

        else:
            login_form = LoginForm()

            form_data = {
              'form': login_form
            }

    else:
        login_form = LoginForm()

    return render(request, 'login.html', form_data)


def Logout(request):
    logout(request)
    return redirect('/')
