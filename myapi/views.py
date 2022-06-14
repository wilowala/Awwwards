from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post, Profile
from .serializers import PostSerializer, ProfileSerializer

# Create your views here.
@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Posts':'/posts/',
        'Profile': '/profiles',
    }
    return Response(api_urls)

@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def profile_list(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)