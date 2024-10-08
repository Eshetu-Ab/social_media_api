from rest_framework.routers import DefaultRouter
from direct_messages.views import MessageViewSet

router = DefaultRouter()
router.register(r'messages', MessageViewSet, basename='message')

urlpatterns = router.urls





