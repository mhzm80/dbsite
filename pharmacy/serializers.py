from rest_framework import serializers
from pharmacy.models import *


class ser_pharmacy(serializers.ModelSerializer):
    class Meta:
        model=ph
        fields="__all__"
