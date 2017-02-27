from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bangazon_ui.models import *
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate


class Login(TemplateView):
    """
    This class is to post user with a username and password to make login possible using post method. This class will use login.html template for users to enter username and password. Once posted it'll redirect to the next page
    Author: Julia Kim-Chung
    """
    template_name = 'bangazon_ui/login.html'

    def post(self, request):

        data=request.POST
        username=data['username']
        password=data['password']
        user=authenticate(
            username=username,
            password=password)
        if user is not None:
            login(request=request, user=user)
        else:
            return HttpResponseRedirect(redirect_to='/register')
        return HttpResponseRedirect(redirect_to='/product_type_list')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(redirect_to='/')