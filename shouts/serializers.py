from rest_framework import serializers
from django.conf import settings 
from profiles.serializers import PublicProfileSerializer

MAX_SHOUT_LENGTH = settings.MAX_SHOUT_LENGTH 
SHOUT_ACTION_OPTIONS = settings.SHOUT_ACTION_OPTIONS


from .models import Shout 




class ShoutCreateSerializer(serializers.ModelSerializer): 
    user = PublicProfileSerializer(read_only=True,source='user.profile')

    likes = serializers.SerializerMethodField(read_only=True)
    nested_parent = serializers.SerializerMethodField(read_only=True)
    did_like = serializers.SerializerMethodField(read_only=True)
    is_same_user = serializers.SerializerMethodField(read_only=True)
    username = serializers.SerializerMethodField(read_only=True)


    class Meta: 
        model = Shout 
        fields = ['user','id','content','likes','nested_parent','did_like','is_same_user','username','timestamp']


    def get_likes(self,obj): 
        return obj.likes.count() 
    def get_nested_parent(self,obj): 
        return obj.parent != None 

    def get_is_same_user(self,obj): 
        return obj.user.username == self.context.get('username')

    def get_username(self,obj): 
        return obj.user.username 

    def validate_content(self,value):
        if(len(value)>MAX_SHOUT_LENGTH): 
            raise serializers.ValidationError("Shout is too long!")
        return value 

    
    def get_did_like(self,obj): 
        username = self.context.get('username')
        did_like = Shout.objects.filter(id=obj.id).first().likes.filter(username = username).exists()
        return did_like 

class ShoutSerializer(serializers.ModelSerializer): 

    user = PublicProfileSerializer(read_only=True,source='user.profile')
    likes = serializers.SerializerMethodField(read_only=True)
    content = serializers.SerializerMethodField(read_only=True)
    parent = ShoutCreateSerializer(read_only=True)
    did_like = serializers.SerializerMethodField(read_only=True)
    is_same_user = serializers.SerializerMethodField(read_only=True)
    username = serializers.SerializerMethodField(read_only=True)

    class Meta: 
        model = Shout 
        fields = ['user','id','content','likes','is_boosted','parent','did_like','children','is_same_user','username','is_boost','timestamp']


    def get_likes(self,obj): 
        return obj.likes.count() 

    def get_content(self,obj):
        return obj.content 

    def get_parent(self,obj): 
        return obj.parent
    def get_is_same_user(self,obj): 
        return obj.user.username == self.context.get('username')

    def get_username(self,obj): 
        return obj.user.username 

    def get_did_like(self,obj): 
        username = self.context.get('username')
        did_like = Shout.objects.filter(id=obj.id).first().likes.filter(username = username).exists()
        return did_like 
    


class ShoutActionSerializer(serializers.Serializer): 

    id = serializers.IntegerField()
    action = serializers.CharField()
    content = serializers.CharField(allow_blank = True,required=False)
    

    

    def validate_action(self,value): 
        if not value in SHOUT_ACTION_OPTIONS: 
            raise serializers.ValidationError("This is not a valid action")
        return value 

