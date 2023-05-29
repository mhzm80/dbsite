from django.urls import path,include
from sick.models import *
from sick.views import *
urlpatterns = [
    path('submit/',sick_uu)
]
