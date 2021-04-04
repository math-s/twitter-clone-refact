from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import include

from assets import views


router = DefaultRouter()
router.register(
  "upload_image", views.ImagesViewSet, basename="upload_image")


urlpatterns = [
    path("", include(router.urls)),
]

app_name = "assets"
