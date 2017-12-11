from django.conf.urls import url, include
from balanca import views
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

from balanca.views import *
from rest_framework import routers, serializers, viewsets
from balanca.views import PesagemViewSet, UserViewSet
from rest_framework import renderers

router = routers.DefaultRouter()
router.register(r'usuario', views.UserViewSet)
router.register(r'groupo', views.GroupViewSet)
router.register(r'peso', views.PesagemViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^balanca/', include('balanca.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
]
