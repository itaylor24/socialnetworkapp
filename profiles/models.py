from django.db import models
from django.conf import settings 
from django.db.models.signals import post_save


User = settings.AUTH_USER_MODEL
# Create your models here.




class FollowerRelation(models.Model): 
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    profile = models.ForeignKey("Profile",on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Profile(models.Model): 
    displayname = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    bio = models.TextField(null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    followers = models.ManyToManyField(User, related_name="following",blank=True)

    def __str__(self): 
        return "Profile - " + self.user.username + ( ": "+  str(self.bio)[:40]  +"..."  if self.bio else ": no bio")


def user_did_save(sender, instance, created, *args, **kwargs): 
    if(created): 
        Profile.objects.get_or_create(user = instance)

post_save.connect(user_did_save,sender=User)