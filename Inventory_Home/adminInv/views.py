# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User


def login(request):
    return render(request,'adminInv/login.html')
def register(request):
	if request.method == "POST":
		fullName = request.POST['fullName']
		username = request.POST['username']
		role = request.POST['role']
		password1 = request.POST['psw']
		password2 = request.POST['pswrepeat']

		user = User(username=username, password=password1, fullName=fullName, role=role, sesskey="123")
		# ToDO: here have to call is valid founction 
		user.save()
		return redirect('login')
	else:
		return render(request,'adminInv/register.html')