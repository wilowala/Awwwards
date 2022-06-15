from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey('Profile', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = CloudinaryField('image', blank = True)
    description = models.TextField(blank=True)
    post_url = models.URLField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['created', '-created']

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    profile_photo = CloudinaryField("image", blank= True)
    bio = models.TextField(blank=True)
    projects = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.user.username

class Rating(models.Model):
    rating = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )

    design = models.IntegerField(choices=rating, default=0, blank=True)
    usability = models.IntegerField(choices=rating, blank=True)
    content = models.IntegerField(choices=rating, blank=True)
    score = models.FloatField(default=0, blank=True)
    design_average = models.FloatField(default=0, blank=True)
    usability_average = models.FloatField(default=0, blank=True)
    content_average = models.FloatField(default=0, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='rater')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings', null=True)

    def save_rating(self):
        self.save()

    @classmethod
    def get_ratings(cls, id):
        ratings = Rating.objects.filter(post_id=id).all()
        return ratings

    def __str__(self):
        return f'{self.post} Rating'