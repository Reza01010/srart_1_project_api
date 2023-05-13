from django.urls import path, include
from .views import jonyur_view, jonyur_user_view
from .views import ItemViewSet
from rest_framework import routers
from myapp.views import ItemViewSet
import myapp
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('j/', jonyur_view, name='jonyur'),
    path('j-u/', jonyur_user_view, name='jonyur_user'),
]
