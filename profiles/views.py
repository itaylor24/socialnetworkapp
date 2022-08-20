from django.shortcuts import render,redirect
from django.http import Http404
from .models import Profile 
from .forms import ProfileForm 



def profile_update_view(request): 
    
    if(not request.user.is_authenticated): 
        return redirect("/login?next=/profile/update")

    user = request.user
    
    my_profile = user.profile 
    user_data = {
        "displayname": my_profile.displayname,
        "email": user.email
    }
    form = ProfileForm(request.POST or None, instance = my_profile , initial=user_data)
    

    if(form.is_valid()): 
        profile_obj = form.save(commit=False)
        displayname = form.cleaned_data.get('display_name')
        email = form.cleaned_data.get('email')
        my_profile.displayname = displayname
        user.email = email
        user.save()
        profile_obj.save()
    context = {"form": form, "btn_label":"Save", "title": "Update Profile"}
    return render(request, "profiles/form.html", context)

# Create your views here.
def profile_detail_view(request,username): 
    qs = Profile.objects.filter(user__username = username)
    if(not qs.exists()): 
        raise Http404
    profile_obj = qs.first()
    context = {"username":username, "is_same_user": 'true' if username == request.user.username else 'false', "profile": profile_obj,"request":request}
    return render(request, "profiles/detail.html",context)
