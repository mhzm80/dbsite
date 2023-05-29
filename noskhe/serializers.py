from rest_framework import serializers
from noskhe.models import *

class ser_noskhe(serializers.ModelSerializer):
    class Meta:
        model=noskhe_h
        fields="__all__"