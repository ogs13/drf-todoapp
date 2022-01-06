from django.db import router
from django.urls import path, include

from rest_framework import routers
from .api import TodoViewSet


router = routers.DefaultRouter()

router.register(r'todos', TodoViewSet)

urlpatterns = [
    path('',include(router.urls)),
    
]

