from django.urls import path, include
from website.views import main_view, book_view
from rest_framework import routers
from website.views import UserViewSet, GroupViewSet, BookViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path("", main_view, name="main"),
    path("<int:pk>", book_view, name="book"),
    path(r'api/', include(router.urls)),
]