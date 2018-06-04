from django.urls import path

from . import views
from authenticate.views import upload_pic
urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='Ssignup'),
]
