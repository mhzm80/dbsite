from rest_framework import serializers
from noskhe.models import *

class ser_noskhe(serializers.ModelSerializer):
    class Meta:
        model=noskhe_h
        fields="__all__"

class answare_user(serializers.ModelSerializer):
    nath_code=serializers.CharField(max_length=200)