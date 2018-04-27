# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
import random
from django.db.models import Q
from .models import RestaurantLocation

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

def restaurant_listview(request):
    template_name = 'restaurants/restaurantlocation_list.html'

    # Allows you to grab data from the database in the form of a list
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)


class RestaurantListView(ListView):
    # The default template: restaurantlocation_list.html
    # is derived using
    # "restaurantlocation" - from the model
    # "_list" - is because its a ListView

    def get_queryset(self):

        # this prints out the query
        print(self.kwargs)
        slug = self.kwargs.get("slug")

        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset


# queryset = RestaurantLocation.objects.filter(category__iexact="mexican")


class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()

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

