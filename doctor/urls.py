from doctor.views import *
from django.urls import path,include

urlpatterns = [
    
    path('doctor/',log_in),
    path('doctor/user/',final_query)
]
