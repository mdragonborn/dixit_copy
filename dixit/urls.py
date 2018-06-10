
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
from django.contrib.auth import views as auth_views
from django.urls import include, path
from game.views import GameView
from django.conf.urls import url
from django.conf.urls.static import static
from dixit import settings
from game  import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cards', views.RetrieveImages)

from accounts import views as accounts_views
from profiles import views as profiles_views

import accounts.urls as accounts_urls
import profiles.urls as profiles_urls
import game.views as game_views
from game.apiviews import CurrentUserView, GameParticipantsView

urlpatterns = [
                  path('admin/', admin.site.urls),

                  url(r'^game/(?P<game_id>\d+)/$', GameView.as_view()),
                  url(r'^img-api/', include(router.urls)),
                  url(r'^upload/$', views.model_form_upload, name='upload'),
                  url(r'^create_game', game_views.create_game, name='create_game'),
                  url(r'^current-user/', CurrentUserView.as_view()),
                  url(r'^game/participants/(?P<game_id>\d+)/$', GameParticipantsView.as_view()),

                  # TODO: Use path instead of url.
                  # TODO: Fix this clusterfuck - subdivide urls by app.
                  url(r'^$', accounts_views.home, name='home'),
                  url(r'^', include(accounts_urls)),
                  url(r'^', include(profiles_urls))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# //////// POLICE LINE DO NOT CROSS //////// POLICE LINE DO NOT CROSS ////////
urlpatterns += static(settings.STATIC_URL, document_root=settings.TEST_DIRECT_STATIC)
