from django.urls import path

from . import views

#in This module will must define the urlspattern.

from django.urls import path

from . import views

urlspatterns = [
    path('', views.index)
    path('New, view.new')
]