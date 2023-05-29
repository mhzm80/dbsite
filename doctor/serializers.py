from rest_framework import serializers
from doctor.models import *
class doc(serializers.ModelSerializer):
    class Meta:
        model=d_doctor
        fields="__all__"
        
class login(serializers.ModelSerializer):
    class Meta:
        model=loginlogin
        fields="__all__"


