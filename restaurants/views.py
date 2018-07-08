# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.db.models import Q # this is for complex lookups with Q objects

from .models import RestaurantLocation
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm

import random

# Create your views here.
# function based view


# def home(request):
#     num = random.randint(1,1000)
#     # return HttpResponse()
#     context = {"html_var": "context variable", "num": num}
#     return render(request, "home.html", context)
#
#
# def about(request):
#     num = random.randint(1,1000)
#     # return HttpResponse()
#     context = {"html_var": "context variable", "num": num}
#     return render(request, "about.html", context)
#
#
# def contact(request):
#     # return HttpResponse()
#     context = {}
#     return render(request, "contact.html", context)


# class HomeView(TemplateView):
#     template_name = 'home.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(HomeView, self).get_context_data(*args, **kwargs)
#         num = random.randint(1, 1000)
#         context = {"html_var": "Menu", "num": num}
#         return context


# METHOD 1: TO CREATE FORM
# def restaurant_createview(request):
#     form = RestaurantCreateForm(request.POST or None)
#     errors = None
#     if form.is_valid():
#         # form validation
#         obj = RestaurantLocation.objects.create(
#             name = form.cleaned_data.get('name'),
#             location = form.cleaned_data.get('location'),
#             category = form.cleaned_data.get('category')
#         )
#         return HttpResponseRedirect("/restaurants/")
#     else:
#         errors = form.errors
#
#     template_name = 'restaurants/form.html'
#     context = {
#         "form": form,
#         "errors": errors
#     }
#     return render(request, template_name, context)

# METHOD 2: TO CREATE FORM
# @login_required(login_url='/login/')
# def restaurant_createview(request):
#     form = RestaurantLocationCreateForm(request.POST or None)
#     errors = None
#     if form.is_valid():
#         if request.user.is_authenticated():
#             instance = form.save(commit=False)
#             instance.owner = request.user
#             instance.save()
#             return HttpResponseRedirect("/restaurants/")
#         else:
#             return HttpResponseRedirect("/login/")
#     if form.errors:
#         errors = form.errors
#
#     template_name = 'restaurants/form.html'
#     context = {
#         "form": form,
#         "errors": errors
#     }
#     return render(request, template_name, context)
#
#
# def restaurant_listview(request):
#     """
#     This is a function base view that can be used in the urls.py to render
#     the view to the DOM
#     """
#
#     template_name = 'restaurants/restaurantlocation_list.html'
#
#     # Allows you to grab data from the database in the form of a list
#     # RestaurantLocation.objects.all() - the call to return the data from the database
#
#     queryset = RestaurantLocation.objects.all()
#
#     # queryset.filter(category__iexact='western') - filtering
#     context = {
#         "object_list": queryset
#     }
#     return render(request, template_name, context)
#
#
# def restaurant_detailview(request, slug):
#     template_name = 'restaurants/restaurantlocation_detail.html'
#     obj = RestaurantLocation.objects.get(slug=slug)
#
#     context = {
#         "object": obj
#     }
#     return render(request, template_name, context)


class RestaurantListView(LoginRequiredMixin, ListView):
    """
    The default template: restaurantlocation_list.html
    is derived using
    "restaurantlocation" - from the model
    "_list" - is because its a ListView
    """

    def get_queryset(self):

        # slug = self.kwargs.get("slug")
        # print("slug: ", slug)
        # if slug:
        #     queryset = RestaurantLocation.objects.filter(
        #         Q(category__iexact=slug) |
        #         Q(category__icontains=slug)
        #     )
        # else:
        #     queryset = RestaurantLocation.objects.all()
        #
        # return queryset

        return RestaurantLocation.objects.filter(owner=self.request.user)


# queryset = RestaurantLocation.objects.filter(category__iexact="mexican")


class RestaurantDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)

    # discovering what the context data returns
    # def get_context_data(self, **kwargs):
    #     print(self.kwargs)
    #     context = super(RestaurantDetailView, self).get_context_data(**kwargs)
    #     print(context)
    #     return context

    # # change "pk" to "rest_id"
    # def get_object(self, **kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     obj = get_object_or_404(RestaurantLocation, id=rest_id)
    #     return obj


# METHOD 3:  TO CREATE FORM
class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantLocationCreateForm
    login_url = '/login/'
    template_name = 'form.html'
    # success_url = "/restaurants/"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        # instance.save()
        return super(RestaurantCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return context


class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    form_class = RestaurantLocationCreateForm
    login_url = '/login/'
    template_name = 'restaurants/detail-update.html '
    # success_url = "/restaurants/"

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
        name = self.get_object().name
        print(name)
        context['title'] = 'Update Restaurant: {0}'.format(name)
        return context

    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)

