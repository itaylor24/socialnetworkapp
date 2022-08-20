from django.db import models
from django.conf import settings 
import random 
from django.db.models import F,Q


User = settings.AUTH_USER_MODEL

class ShoutLike(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shout = models.ForeignKey("Shout", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
class ShoutQuerySet(models.QuerySet): 
    def feed(self,user): 
        profiles_exist = user.following.exists()
        followed_users_id = []
        
        if(profiles_exist):
            followed_users_id = user.following.values_list("user__id",flat=True)
            
        return self.filter(Q(user__id__in = followed_users_id) | Q(user=user)).order_by("-timestamp")

class ShoutManager(models.Manager):
    def get_query_set(self,*args,**kwargs): 
        return ShoutQuerySet(self.model, using=self._db)
    def feed(self,user): 
        return self.get_query_set().feed(user)

# Create your models here.
class Shout(models.Model):
   
    thread_parent = models.ForeignKey("self", related_name="thread_parent_shout",null=True,on_delete=models.SET_NULL,blank=True)
    parent = models.ForeignKey("self",related_name="parent_shout", null=True,on_delete=models.SET_NULL,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="shouts")
    likes = models.ManyToManyField(User, related_name='shout_user',blank=True,through=ShoutLike)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)

    objects = ShoutManager()
    class Meta: 
        ordering = ['-id']
        
        
    @property 
    def is_boost(self): 
        return self.parent!=None 
        
    @property  
    def is_boosted(self): 
        return Shout.objects.filter(parent = self).exists()

    def children(self):
        fields = tuple(x.name for x in Shout._meta.get_fields())
        children =  Shout.objects.filter(thread_parent = self).values(*fields, username=F("user__username"),user_displayname=F("user__profile__displayname"))
        return children

    def username(self): 
        username = self.user.username 
        return username 

    def __str__(self): 
        return "Shout" + str(self.id) + ": " + (self.content if self.content else "No content")