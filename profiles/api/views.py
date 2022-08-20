from re import I
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings 
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


from django.contrib.auth import get_user_model 

from ..models import Profile  
from ..serializers import PublicProfileSerializer




User = get_user_model()

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.

'''@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def user_follow_view(request,username): 
    current_user = request.user 
    other_user_qs = User.objects.filter(username = username)

    if other_user_qs.exists() == False: 
        return Response({},status = 404)

    other_user = other_user_qs.first()
    profile = other_user.profile

    
    if current_user.username == username: 
        my_followers_qs = profile.followers.all()
        return Response({"count":my_followers_qs.count()},status=400)

    
    
    
    current_followers_qs = profile.followers.all()
    serializer = PublicProfileSerializer(instance=profile,context={"request":request})
    return Response(serializer.data,status=200)'''


@api_view(['GET','POST'])
def profile_detail_api_view(request,username): 



    qs = Profile.objects.filter(user__username = username)
    if(not qs.exists()): 
        return Response({"detail":"user not found"},status=400)
    
    data = request.data or {}
    


    profile_obj = qs.first()
    if(request.method=="POST"):
        action = data.get("action")
        if(profile_obj.user != request.user):
            if(action == "follow"): 
                profile_obj.followers.add(request.user)
            elif(action == "unfollow"): 
                profile_obj.followers.remove(request.user)

    
    
    serializer = PublicProfileSerializer(instance=profile_obj,context={"request":request})
    
    return Response(serializer.data,status=200)