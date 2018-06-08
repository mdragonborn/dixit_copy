from django.conf.urls import url

from profiles import views as profiles_views

urlpatterns = [
    url(r'^profile/$', profiles_views.profile, name='profile'),
    url(r'^profile/edit$', profiles_views.profile_edit,
        name='profile_edit')
]
