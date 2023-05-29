from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sick.serializers import sick_user


# Create your views here.

@api_view(['GET','POST'])
def sick_uu(request):
    if request.method=="GET":
        return Response({'this':'GET'})
    else:
        ser=sick_user(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        else:
            return Response(ser.errors)