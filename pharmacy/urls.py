 
from django.urls import path,include
from pharmacy.views import *
urlpatterns = [
    
    path('daro/',list_ph)
    
]