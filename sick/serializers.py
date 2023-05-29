from .models import *
from rest_framework import serializers


class sick_user(serializers.ModelSerializer):
    class Meta:
        model=sick
        fields="__all__"
        read_only_fields=(['statuc'])
        
        