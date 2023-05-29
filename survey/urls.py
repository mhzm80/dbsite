from django.urls import path,include
from survey.views import survey_1
urlpatterns = [
    path('survey/',survey_1)
]


