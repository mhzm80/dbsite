from .models import *
from rest_framework import serializers


class survey_ser(serializers.ModelSerializer):
    class Meta:
        model=survey_u
        fildes="__all__"
