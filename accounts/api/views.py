from re import I
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings 
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model 







User = get_user_model()

@api_view(['POST'])
def create_account_view(request):


    username = request.data['username']
    email = request.data['email']
    password = request.data['password']
    


    
    if(User.objects.filter(username=username).exists()): 
        return Response({"response":"Choose another username"},status=401)


    user = User.objects.create_user(username=username,
                                 email=email,
                                 password=password)

    token = Token.objects.get(user=user).key

    return Response({"response":"Account created successfully", "token": token},status=200)