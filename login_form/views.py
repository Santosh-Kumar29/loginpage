# from django.shortcuts import render
from cmath import e
from distutils.log import error

import json
from logging import exception
from tkinter import E
from django.http import HttpResponse
# import jason
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from simplejson import dump
from login_form import models
from login_form import serializers
from login_form.models import login_page
from login_form.serializers import isactiveserializer, logformserializer, logvieweserializer


#################################################################################



@api_view(['POST'])
def login_adddata(request):
    print("======= Login Form POST Operation =========")
    requestdata = json.loads(request.body.decode("utf-8"))
    data1 = requestdata.get("username")
    data2 = requestdata.get("email_id")

    dumpcheck = models.login_page.objects.filter(username = data1)
    
    dumpcheck2 = models.login_page.objects.filter(email_id = data2)

    if dumpcheck:
            return HttpResponse(json.dumps({"status":500, "msg": "username already exist"}))
    elif dumpcheck2:
        return HttpResponse(json.dumps({"status":500, "msg": "email id already exist"}))

    else:
        serializer = logformserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "Data Created Successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)




##########################################################################################


@api_view(['GET'])
def login_getdata(request):
    print("======= Login Form GET Operation =========")
    body = json.loads(request.body.decode("utf-8"))
    username1 = body.get("username")
    password = body.get("password")

    # is_active = login_page.objects.filter(is_active = True)



    # dumpcheck = login_page.objects.get(is_active = activedata)
    # print(activedata)
    # user_isactive = models.login_page.objects.get(username = username)
    # active = models.login_page.get(id == True)    
    # member = models.login_page.objects.get(is_active = True)
    # print(active)

        # print(activedata)
    # if dumpcheck:
    # dumcheck = is_active = activedata
    # if dumcheck:
    # dumpcheck = login_page.objects.filter(is_active = True)
    # , is_active = True)
    # print(member)

    try:
        member = login_page.objects.get(username = username1, password=password)
        if member.is_active:
            serializers = isactiveserializer(member)
            return Response({"status": "Data", "data": serializers.data})
        else:
            return HttpResponse(json.dumps({"status":500, "msg": "This user does not exist"}))
    except Exception as e:
         return Response({"status": "error", "data": serializers.errors}, status=status.HTTP_400_BAD_REQUEST)
        # print(e)
        # return HttpResponse(json.dumps({"status":500, "msg": "This user does not exist"}))
        


     
######################################################################################

@api_view(['GET'])
def login_isactivaedata(request):
    print("============== Login Form is_activate validation ===============")
    body = json.loads(request.body.decode("utf-8"))
    username1 = body.get("username")
    
    try:
        member = models.login_page.objects.get(username = username1)
        serializers = isactiveserializer(member)
        return Response({"status": "Data", "data": serializers.data})
    except:
         return Response({"status": "username does not exist"})



##################################################################################
@api_view(['PUT'])
def login_isactiveput(request):
    print("============== Login Form is_active update")
    body = json.loads(request.body.decode("utf-8"))
    username = body.get("username")

    try:
        member = models.login_page.objects.get(username = username)
        serializers = isactiveserializer(member, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"status": "Data update successfully", "data": serializers.data})
    except:
         return Response({"status": "username does not exist"})
