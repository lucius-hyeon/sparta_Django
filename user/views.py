from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def sign_up(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        phone = request.POST.get('phone', None)
        address = request.POST.get('address', None)

        UserModel.objects.create_user(
            username=username, password=password, phone=phone, address=address)

        return redirect('/login')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        print(username, password)

        me = auth.authenticate(request, username=username, password=password)

        if me is not None:
            print("로그인 성공?")
            auth.login(request, me)
            return redirect('/home')
        else:
            print("로그인 실패?")
            return redirect('/login')

    elif request.method == "GET":
        user = request.user.is_authenticated
        if user:
            return redirect('/home')
        else:
            print('실패')
            return render(request, 'user/login.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')
