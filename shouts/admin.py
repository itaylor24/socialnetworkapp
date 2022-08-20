from django.contrib import admin

# Register your models here.
from .models import Shout, ShoutLike




class ShoutLikeAdmin(admin.TabularInline): 
    model = ShoutLike 
    
class ShoutAdmin(admin.ModelAdmin):
    inlines = [ShoutLikeAdmin]
    list_display = ['__str__','user']
    search_fields = ['content','user_username','user_email']
    class Meta: 
        model = Shout 

admin.site.register(Shout,ShoutAdmin)