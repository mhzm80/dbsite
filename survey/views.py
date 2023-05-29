from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from survey.models import *
from survey.srializers import *


# Create your views here.

@api_view(['POST','GET'])
def survey_1(request):
    if requets.method=="POST":
        ser=survey_ser(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        else:
            return Response(ser.errors)
    else:
        Response({"method":"GET"})

