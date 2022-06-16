from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import SignupView, UserView

urlpatterns = [
    path("signup/", SignupView.as_view()),
    # path("login/", LoginView.as_view()),
    path("me/", UserView.as_view()),
    # path("logout/", LogoutView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
