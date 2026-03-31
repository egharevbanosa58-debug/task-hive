from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('me/', views.ProfileView.as_view(), name='profile'), # Some Optional Shii
    path('token/refresh/', TokenRefreshView.as_view()), # To keep Users logged in
    path('logout/', views.LogoutView.as_view(), name='logout'), # To log out users
]