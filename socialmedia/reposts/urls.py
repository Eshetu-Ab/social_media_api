from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RepostViewSet

router = DefaultRouter()
router.register(r'', RepostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
