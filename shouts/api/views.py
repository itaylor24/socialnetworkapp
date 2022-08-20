from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings 
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from ..serializers import ShoutSerializer, ShoutActionSerializer, ShoutCreateSerializer
from ..models import Shout 
from ..forms import ShoutForm 
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication





ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def shout_create_view(request): 
    serializer = ShoutCreateSerializer(data=request.data,context={'username' :request.user.username})


    if serializer.is_valid(raise_exception=True): 
        serializer.save(user=request.user)
        return Response(serializer.data,status=201)
    return Response({},status=400)

@api_view(['GET'])
def shout_list_view(request, *args, **kwargs): 
    qs = Shout.objects.all()
    qs = qs.filter(thread_parent__isnull=True)
    username = request.GET.get('username') #?username = ?? 
    if(username !=None):
        qs = qs.filter(user__username__iexact=username)
    return get_paginated_queryset_response(qs,request)

def get_paginated_queryset_response(qs,request,size=20): 
    paginator = PageNumberPagination()
    paginator.page_size = size
    paginated_qs = paginator.paginate_queryset(qs, request)
    serializer = ShoutSerializer(paginated_qs, many=True,context={'username' :request.user.username,"request":request})
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def shout_feed_view(request, *args, **kwargs): 

    user = request.user
    qs_all = Shout.objects.feed(user)
    print(user)
    qs = qs_all.filter(thread_parent__isnull=True)
    
    return get_paginated_queryset_response(qs,request)#Response(serializer.data,status=200)

@api_view(['GET'])
def shout_detail_view(request,shout_id, *args, **kwargs): 
    qs = Shout.objects.filter(id=shout_id)
    if(not qs.exists()): 
        return Response({},status=404)    
    obj = qs.first()
    serializer = ShoutSerializer(obj,context={'username' :request.user.username})
    return Response(serializer.data,status=200)

@api_view(['DELETE','POST'])
@permission_classes([IsAuthenticated])
def shout_delete_view(request,shout_id, *args, **kwargs): 
    qs = Shout.objects.filter(id=shout_id)
    if(not qs.exists()): 
        return Response({},status=404)   
    qs = qs.filter(user=request.user)
    if(not qs.exists()): 
        return Response({"message":"You are unauthorized to delete this shout"},status=401)
    obj = qs.first()
    obj.delete()
    return Response({"shout removed"},status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def shout_action_view(request, *args, **kwargs): 
    '''
    id is required
    Action options are Like, Unlike, Reply and Boost
    '''

    serializer = ShoutActionSerializer(data=request.data)

    if(serializer.is_valid(raise_exception = True)): 
        data = serializer.validated_data 
        
        shout_id = data.get("id")
        action = data.get("action")
        content = data.get("content")
        did_like = data.get('did_like')

    qs = Shout.objects.filter(id=shout_id)
    if(not qs.exists()): 
        return Response({},status=404) 
    obj = qs.first()
    if(action == "like"):

        obj.likes.add(request.user)
        serializer = ShoutSerializer(obj,context ={'username' :request.user.username})
   
        return Response(serializer.data,status=200)

    elif(action == "unlike"): 

        obj.likes.remove(request.user)
        serializer = ShoutSerializer(obj,context ={'username' :request.user.username})
     

        return Response(serializer.data,status=200)

    elif(action == "boost"): 
        new_obj = Shout.objects.create(user=request.user,parent=obj,content=content)
        serializer = ShoutSerializer(new_obj,context ={'username' :request.user.username})
        return Response(serializer.data,status=201)

    elif(action == "reply"): 

        new_obj = Shout.objects.create(user = request.user, content = content, thread_parent = obj)
        obj.save()
        serializer = ShoutSerializer(obj,context = {'username' :request.user.username})
        return Response(serializer.data,status=201)

    return Response({},status=200)
