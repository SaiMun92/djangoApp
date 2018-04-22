# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.
# function based view


def home(request):
    num = random.randint(1,1000)
    # return HttpResponse()
    context = {"html_var": "context variable", "num": num}
    return render(request, "home.html", context)


def about(request):
    num = random.randint(1,1000)
    # return HttpResponse()
    context = {"html_var": "context variable", "num": num}
    return render(request, "about.html", context)


def contact(request):
    num = random.randint(1,1000)
    # return HttpResponse()
    context = {"html_var": "context variable", "num": num}
    return render(request, "contact.html", context)
