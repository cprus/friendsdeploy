# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login.models import users
from .models import friends
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'friends': friends.objects.filter(flist=users.objects.get(id=request.session['user_id'])),
        'user': users.objects.get(id = request.session['user_id']),
        'allusers': users.objects.all()

    }
    return render(request, 'friend/landing.html', context)

def show(request, emailuser):
    context = {
        'user': users.objects.get(email=emailuser)
    }
    return render(request, 'friend/show.html', context)

def remove(request, friend_id):
    b = friends.objects.get(id = friend_id)
    b.delete()
    return redirect('/home')

def add(request, user_id):
    a = users.objects.get(id = user_id)
    new_friend = {
        'name': a.name,
        'email': a.email,
        'flist': users.objects.get(id=request.session['user_id'])
    }
    friends.objects.create(name= new_friend['name'], email = new_friend['email'], flist = new_friend['flist'])

    return redirect('/home')
