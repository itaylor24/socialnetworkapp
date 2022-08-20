from django import forms 
from django.conf import settings 

from .models import Shout


MAX_SHOUT_LENGTH = settings.MAX_SHOUT_LENGTH


class ShoutForm(forms.ModelForm):
    class Meta: 
        model = Shout 
        fields = ['content']
    def clean_content(self): 
        content = self.cleaned_data.get("content")

        if(len(content)>MAX_SHOUT_LENGTH): 
            raise forms.ValidationError("Shout is too long!")

        return content 
