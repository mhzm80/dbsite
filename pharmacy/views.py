from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pharmacy.serializers import *
from pharmacy.models import *

# Create your views here.

@api_view(['GET'])
def list_ph(request):
    if request.method=="GET":
        
        a=ph.objects.all()
        ser=ser_pharmacy(a,many=True)
        return Response(ser.data)
    else:
        return Response({'method':'notget'})
    