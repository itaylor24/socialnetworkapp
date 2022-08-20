from django import forms 
from django.contrib.auth import get_user_model

from .models import Profile 


User = get_user_model 



class ProfileForm(forms.ModelForm): 

    display_name = forms.CharField(required=False)
    email = forms.CharField(required = False)

    class Meta: 
        model = Profile 
        fields = [ 'bio']

