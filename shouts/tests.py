from django.test import TestCase
from .models import Shout 
from django.contrib.auth import get_user_model 
from rest_framework.test import APIClient 

User = get_user_model()

# Create your tests here.
class ShoutTestCase(TestCase): 
    def setUp(self):
        self.user = User.objects.create_user(username='test_user1', password='test_password1')
        Shout.objects.create(content="my first shout", user=self.user)
        Shout.objects.create(content="my second shout", user=self.user)
        Shout.objects.create(content="my third shout", user=self.user)
        self.currentCount = Shout.objects.all().count()

    def test_user_created(self): 
        self.assertEqual(self.user.username,'test_user1')

    def test_shout_created(self): 
        shout_obj = Shout.objects.create(content='my shout', user=self.user)
        self.assertEqual(shout_obj.id,4)
        self.assertEqual(shout_obj.user, self.user)
    
    def get_client(self): 
        client = APIClient()
        client.login(username = self.user.username, password = 'test_password1')
        return client

    def test_shout_list(self): 
        client = self.get_client()
        response = client.get("/api/shouts/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()),3)


    def test_action_like(self): 
        client = self.get_client()
        response = client.post("/api/shouts/action/",{"id":2,"action":"like"})
        self.assertEqual(response.status_code, 200)


    def test_action_unlike(self): 
        client = self.get_client()
        response = client.post("/api/shouts/action/",{"id":2,"action":"like"})
        self.assertEqual(response.status_code, 200)
        response = client.post("/api/shouts/action/",{"id":2,"action":"unlike"})
        self.assertEqual(response.status_code, 200)
        like_count = response.json().get("likes")
        self.assertEqual(like_count,0)
        
    def test_action_boost(self): 
        client = self.get_client()
        response = client.post("/api/shouts/action/",{"id":2,"action":"boost"})
        self.assertEqual(response.status_code, 201)
        data= response.json()
        new_id = data.get("id")
        self.assertNotEqual(2,new_id)
    
    
    def test_shout_create_api(self): 
        request_data = {"content": "New shout test"}
        client = self.get_client()
        response = client.post("/api/shouts/create/")
        self.assertEqual(response.status_code, 201)
        response_data= response.json()
        new_id = response_data.get("id")
        self.assertEqual(self.currentCount+1,new_id)
        