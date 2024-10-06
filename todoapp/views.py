from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializer import *
# Create your views here.
@api_view(['GET'])
def task_list(request):
    taskdata=Task.objects.all()
    serial=TaskSerial(taskdata,many=True)
    return Response(data=serial.data)

@api_view(['POST'])
def task_create(request):
    if request.method=='POST':
        serial=TaskSerial(data=request.data)
        if serial.is_valid():
            serial.save()
            print('data inserted...')
            return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def task_detail(request,id):
    try:
        taskdata=Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    serial=TaskSerial(taskdata)
    return Response(data=serial.data,status=status.HTTP_200_OK)

@api_view(['GET','PUT'])
def task_update(request,id):
    try:
        taskid=Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method=='GET':
        serial=TaskSerial(taskid)
        return Response(data=serial.data,status=status.HTTP_200_OK)

    if request.method=='PUT':
        serail=TaskSerial(data=request.data,instance=taskid)
        if serail.is_valid():
            serail.save()
            return Response(status=status.HTTP_200_OK)
        
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','DELETE'])
def task_delete(request,id):
    try:
        taskid=Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method=='GET':
        serial=TaskSerial(taskid)
        return Response(data=serial.data,status=status.HTTP_200_OK)

    if request.method=='DELETE':
        Task.delete(taskid)
        return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PATCH'])
def task_select_update(request,id):
    try:
        taskid=Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method=='GET':
        serial=TaskSerial(taskid)
        return Response(data=serial.data,status=status.HTTP_200_OK)
    
    if request.method=='PATCH':
        serail=TaskSerial(data=request.data,instance=taskid,partial=True)
        if serail.is_valid():
            serail.save()
            return Response(status=status.HTTP_200_OK)
        
    return Response(status=status.HTTP_400_BAD_REQUEST)
    


            

