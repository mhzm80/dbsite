from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from doctor.serializers import *
from sick.models import *
from sick.serializers import *
# Create your views here.


@api_view(['POST','GET'])
def log_in(request):
    if request.method=="POST":

        ser=login(data=request.data)
        if ser.is_valid():
            a=d_doctor.objects.filter(Username=ser.data["username"])
            a=a.filter(Password=ser.data["password"])
        
            if len(a)==0:
                return Response()
            else:

                return Response(1)
            

        else:
            return Response({'answare':'bad'})

    else:
        A=sick.objects.all()
        x=sick_user(A,many=True)
        return Response(x.data)


@api_view(['GET'])
def final_query(request):
    e=sick.objects.filter(id=request.query_params['id'])
    if e:
        ser=sick_user(e,many=True)
        return Response(ser.data)
    else:
        return Response()