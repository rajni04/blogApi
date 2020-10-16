from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,RetrieveUpdateAPIView,CreateAPIView,DestroyAPIView
from blogapp.models import Post
from blogapp.serializers import PostSerializer, PostCreateUpdateSerializer,LoginSerializer,RegistrationSerializer

from rest_framework.generics import GenericAPIView
from django.contrib.auth import login as django_login
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from django.contrib.auth import login as django_login
from rest_framework.views import APIView
#from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser,IsAuthenticatedOrReadOnly,AllowAny
from rest_framework.authtoken.models import Token

from .permissions import IsOwnerOrReadOnly



from rest_framework.response import Response

# Create your views here.


User = get_user_model()
class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

class RegisterListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

class LoginAPIView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)
    

"""class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        django_logout(request)
        return Response(status=204)"""

class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class =  PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def post_create(self,serializer):
        serializer.save(user=self.request.user)

   
class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

class PostDetailAPIView(RetrieveAPIView):
    queryset =Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]


class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsOwnerOrReadOnly]
    def post_update(self,serializer):
        serializer.save(user=self.request.user)


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    
