from django.urls import path
from .views import index
from .user_views import signup

urlpatterns = [
    path('', index, name="index"),
    #user urls
    path('signup', signup, name='signup'),
]
