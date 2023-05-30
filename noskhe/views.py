from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from noskhe.serializers import *
from noskhe.models import *
from sick.models import *
# Create your views here.

@api_view(['POST'])
def an_noskhe(request):
    ser=ser_noskhe(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data)
    else:
        return Response(ser.errors)



@api_view(['POST'])
def answare(request):
    a=request.data['Nationalcode']
    x=answare_user(a,many=True)
    if x.is_valid():
        m=sick.objects.filter(Nationalcode=x.data['nath_code'])
        m=m.filter(statuc=True)
        if m:
            return Response(m.data)
        else:
            return Response({'answare':'no national code'})
