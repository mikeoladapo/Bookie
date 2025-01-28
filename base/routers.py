from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet,CategoryViewSet,BookViewSet,AuthorViewSet

router = DefaultRouter()
router.register(r"users",CustomUserViewSet,basename="user")
router.register(r"categories",CategoryViewSet,basename="category")
router.register(r"books",BookViewSet,basename="book")
router.register(r"authors",AuthorViewSet,basename="user")


urlpatterns = router
