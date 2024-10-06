from rest_framework import serializers
from .models import *

class Apiserial(serializers.ModelSerializer):
    class Meta:
        model=ApiPath
        fields='__all__'