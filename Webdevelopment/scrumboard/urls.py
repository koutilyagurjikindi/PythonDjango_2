from rest_framework.routers import DefaultRouter
from .api import ListViewSet,CardViewSet

router = DefaultRouter()
router.register(r'cards',CardViewSet)
router.register(r'lists',ListViewSet)

urlpatterns = router.urls
