from django.shortcuts import render
from django.conf import settings 
from django.shortcuts import redirect







ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.

def home_view(request):
    if(request.user.username == ""): 
        return redirect('/login')

    return render(request,'pages/feed.html',context={"username":request.user.username})

def shout_list_view(request): 

    if(request.user.username == ""): 
        return redirect('/login')
    return render(request, "shouts/list.html", context={"username": request.user.username})

def shout_detail_view(request, shout_id): 
    if(request.user.username == ""): 
        return redirect('/login')
    return render(request, "shouts/detail.html",context={"shout_id":shout_id,"username": request.user.username})

def shout_profile_view(request, username): 
    if(request.user.username == ""): 
        return redirect('/login')
    is_same_user = request.user.username == username
 
    return render(request, "shouts/profile.html",context={"profile_username": username, "is_same_user": 'true' if is_same_user else 'false',"username": request.user.username})

