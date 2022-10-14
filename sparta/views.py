from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def home(request):
    return render(request, 'home.html')
