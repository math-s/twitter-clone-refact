from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

app_name = "accounts"

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="obtain_jwt_token"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh_jwt_token")
]
