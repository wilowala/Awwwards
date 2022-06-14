from django.test import TestCase
from .models import  Post, Profile 
from django.contrib.auth.models import User

# Create your tests here.
class ImageTest(TestCase):
    def setUp(self):
        self.new_user = User(username='wilowala')
        self.new_user.save()
        self.new_profile = Profile(bio='coder', user=self.new_user)
        self.new_profile.save()
        self.new_post = Post(owner= self.new_profile, title='Life', description='Tenatous and spry as always')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post, Post))

    def test_save_method(self):
        self.new_post.save()
        images = Post.objects.all()
        self.assertTrue(len(images) > 0 )

    def test_delete_method(self):
        self.new_post.save()
        self.new_post.delete()
        images = Post.objects.all()
        self.assertTrue(len(images) == 0 )

    def test_update_profile(self, new_profile):
        self.new_post.save()
        self.new_profile.update_profile(id=new_profile)