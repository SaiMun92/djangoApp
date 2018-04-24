# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
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
    # return HttpResponse()
    context = {}
    return render(request, "contact.html", context)


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        num = random.randint(1, 1000)
        context = {"html_var": "Menu", "num": num}
        return context

