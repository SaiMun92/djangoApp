# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# For creating database schema?
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse

from .utils import unique_slug_generator
from .validators import validate_category

User = settings.AUTH_USER_MODEL


# Create your models here.
class RestaurantLocation(models.Model):
    owner     = models.ForeignKey(User)
    name      = models.CharField(max_length=120)
    location  = models.CharField(max_length=120, null=True, blank=True)
    category  = models.CharField(max_length=120, null=True, blank=True, validators=[validate_category])
    timestamp = models.DateTimeField(auto_now_add=True)
    updated   = models.DateTimeField(auto_now=True)
    slug      = models.SlugField(null=True, blank=True)
    #my_date_field = models.DateField(auto_now=False, auto_now_add=False)

    # Display the name of the content in the database
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('restaurants:detail', kwargs={'slug': self.slug})
        # namespace: name

    @property
    def title(self):
        return self.name


# signal to the terminal that something has been saved to the database from the admin
def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    print('saving...')
    print(instance.timestamp)

    # save the category in a capitalize format
    instance.category = instance.category.capitalize()
    # if the slug field is empty, call the unique slug generator
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


# def rl_post_save_receiver(sender, instance, *args, **kwargs):
#     print('saved')
#     print(instance.timestamp)


pre_save.connect(rl_pre_save_receiver, sender=RestaurantLocation)

# post_save.connect(rl_pre_save_receiver, sender=RestaurantLocation)
