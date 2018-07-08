from django.conf.urls import url, include


from django.contrib.auth.views import LoginView


from .views import (
    ItemListView,
    ItemCreateView,
    ItemDetailView,
    ItemUpdateView
)

urlpatterns = [
    url(r'^$', ItemListView.as_view(), name='list'),
    url(r'^create/$', ItemCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', ItemUpdateView.as_view(), name='detail'),
    # url(r'^(?P<pk>\d+)/edit/$', ItemUpdateView.as_view(), name='update'),
]

