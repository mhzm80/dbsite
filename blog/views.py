from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import *
from blog.serializers import *
# Create your views here.

@api_view(['GET'])
def ap_de_blog(request):
    a=blog_new.objects.all()
    x=ser_blog(a,many=True)
    return Response(x.data)