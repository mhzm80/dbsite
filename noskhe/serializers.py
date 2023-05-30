from rest_framework import serializers
from noskhe.models import *

class ser_noskhe(serializers.ModelSerializer):
    class Meta:
        model=noskhe_h
        fields="__all__"

class answare_user(serializers.Serializer):
    Nationalcode=serializers.CharField(max_length=200,required=True)