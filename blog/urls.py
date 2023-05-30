
from django.urls import path,include
from blog.views import *
urlpatterns = [
    
    path('blog_news/',ap_de_blog),
    path('add/',take)
]

