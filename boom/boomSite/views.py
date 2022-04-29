import chunk
from fileinput import filename
from multiprocessing import context
from tkinter import S
from django.shortcuts import render, redirect
from django.http import HttpResponse, StreamingHttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import NewUserForm
from .forms import NewPlayerForm
import json
from json import dumps, load, loads
from django.views.decorators.csrf import csrf_exempt
import ast #para diccionario
import sqlite3
from django.contrib.auth.models import User
from .models import Player
from .models import Global
from .models import Plays
from django.contrib.auth.decorators import login_required   
import hashlib
import mimetypes
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import os


def index(request):
    template = loader.get_template('boomSite/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

# def download(request):
    

def about(request):
    template = loader.get_template('boomSite/about.html')
    context = {}
    return HttpResponse(template.render(context, request))

def stats(request):
    
    mydb = sqlite3.connect("db.sqlite3")
    curr = mydb.cursor()

    #Gráfica de Niveles
    hl1 = 'Username'
    hl2 = 'Level'
    nivelesJugadores = curr.execute("SELECT username, level FROM boomSite_global ORDER BY level ASC")
    successlj = [[hl1 , hl2]]
    
    for y in nivelesJugadores:
        successlj.append([y[0], y[1]])
    nivelesJugadores = dumps(successlj)


    return render(request, 'boomSite/stats.html', {'niveles':nivelesJugadores})
