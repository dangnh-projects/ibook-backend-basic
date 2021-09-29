from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path('api/login', jwt_views.TokenObtainPairView.as_view(), name='LoginView'),
    path('api/run', views.HelloWorldView.as_view(), name='HelloWorldView'),
    path('api/me', views.ExtractTokenView.as_view(), name='ExtractTokenView'),
]
