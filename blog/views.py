from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import *
from blog.serializers import *
# Create your views here.

@api_view(['GET'])
def ap_de_blog(request):
    a=blog_new1.objects.all()
    x=ser_blog(a,many=True)
    return Response(x.data)
@api_view(['POST'])
def take(request):
    ser=ser_blog(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response({'answare':'save in database'})