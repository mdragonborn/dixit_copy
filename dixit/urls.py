"""dixit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as dj_auth_views

from authenticate import views as auth_views

urlpatterns = [url(r'^$', auth_views.home, name='home'),
               url(r'^signup/$', auth_views.signup, name='signup'),
               url(r'^admin/', admin.site.urls),
               url(r'^upload/$', auth_views.model_form_upload, name='upload'),
               url(r'^login/$', dj_auth_views.LoginView.as_view(template_name='authenticate/login.html'), name='login'),
               url(r'^logout/$', dj_auth_views.LogoutView.as_view(), name='logout'),
               url(r'^reset/$',
                   dj_auth_views.PasswordResetView.as_view(
                       template_name='authenticate/password_reset.html',
                       email_template_name='authenticate/password_reset_email.html',
                       subject_template_name='authenticate/password_reset_subject.txt'
                   ),
                   name='password_reset'),
               url(r'^reset/done/$',
                   dj_auth_views.PasswordResetDoneView.as_view(template_name='authenticate/password_reset_done.html'),
                   name='password_reset_done'),
               url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                   dj_auth_views.PasswordResetConfirmView.as_view(
                       template_name='authenticate/password_reset_confirm.html'),
                   name='password_reset_confirm'),
               url(r'^reset/complete/$',
                   dj_auth_views.PasswordResetCompleteView.as_view(
                       template_name='authenticate/password_reset_complete.html'),
                   name='password_reset_complete'),

               url(r'^settings/password/$',
                   dj_auth_views.PasswordChangeView.as_view(template_name='authenticate/password_change.html'),
                   name='password_change'),
               url(r'^settings/password/done/$',
                   dj_auth_views.PasswordChangeDoneView.as_view(template_name='authenticate/password_change_done.html'),
                   name='password_change_done'),
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
