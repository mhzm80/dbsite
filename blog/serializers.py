from rest_framework import serializers
from blog.models import *
class ser_blog(serializers.ModelSerializer):
    class Meta:
        model=blog_new
        fields="__all__"


