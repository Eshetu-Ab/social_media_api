from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HashtagViewSet

router = DefaultRouter()
router.register(r'', HashtagViewSet)  #  'hashtags' to '' for direct access

urlpatterns = [
    path('', include(router.urls)),
]
