from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views.generic import FormView

from .forms import LoginForm


class LoginView(FormView):

    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/'

    def form_valid(self, form):
        return super(LoginView, self).form_valid(form)


def Logout(request):
    logout(request)
    return redirect('/')
