from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def apioverview(request):
    try:
        apidata=ApiPath.objects.all()
    except ApiPath.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    serial=Apiserial(apidata,many=True)
    return Response(data=serial.data,status=status.HTTP_200_OK)
