from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.api_overview, name='apiOverview'),
    path('posts/', views.post_list, name='posts'), 
    path('profiles/', views.profile_list, name='profiles'), 
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)