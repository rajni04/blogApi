from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import(
    PostListAPIView,
    PostDetailAPIView,
    PostUpdateAPIView,
    PostCreateAPIView, 
    RegisterListAPIView,
    LoginView,
    LogoutView,
    RegisterAPIView
)


urlpatterns = [
    
    path('list', PostListAPIView.as_view(), name='list'),
    path('list/<int:pk>/', PostDetailAPIView.as_view()),
    path('list/<int:pk>/edit/', PostUpdateAPIView.as_view(),name='edit'),
    path('create', PostCreateAPIView.as_view(), name='create'),
    path('auth/',obtain_auth_token),
    path('registeruser/', RegisterAPIView.as_view(), name='registeruser'),
    path('userlist', RegisterListAPIView.as_view(), name='userlist'),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),

]