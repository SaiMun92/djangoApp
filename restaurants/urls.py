from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
# from restaurants.views import HomeView

from django.contrib.auth.views import LoginView


from .views import (
    # restaurant_createview,
    # restaurant_listview,
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreateView
)

urlpatterns = [
    url(r'^$', RestaurantListView.as_view(), name='list'),
    url(r'^create/$', RestaurantCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name='detail'),
]

