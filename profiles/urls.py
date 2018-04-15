from django.urls import path

from . import views

from profiles import views as v


urlpatterns = [
    path('', views.profile, name='profile'),
    path('signup', v.signup, name = 'signup'),
]
