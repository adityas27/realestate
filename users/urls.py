from django.urls import path, include
from .views import sign_in, sign_out, profile,sign_up, profile_update
urlpatterns = [
    path('login/', sign_in, name='login'),
    path('logout/', sign_out, name='logout'),
    path('profile/', profile, name='profile'),
    path('register/', sign_up, name='register'),
    path('profileupdate/', profile_update, name='update'),
]
