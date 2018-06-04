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
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
