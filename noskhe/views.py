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
    # return Response(request.data)
    x=answare_user(data=request.data)
    if x.is_valid():

        m=sick.objects.filter(Nationalcode=x.data['Nationalcode'])
        m=m.filter(statuc=True)
        if m:
            
            zz=noskhe_h.objects.filter(Uid=m[0].id)
            return Response(zz[0].Ideadoctor)
        else:
            return Response({'answare':'no national code'})
