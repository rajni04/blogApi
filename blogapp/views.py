from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,RetrieveUpdateAPIView,CreateAPIView
from blogapp.models import Post
from blogapp.serializers import PostSerializer,PostCreateSerializer,LoginSerializer,RegistrationSerializer

from rest_framework.generics import GenericAPIView
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import login as django_login
from rest_framework.views import APIView
#from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser,IsAuthenticatedOrReadOnly,AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from .permissions import IsOwnerOrReadOnly



from rest_framework.response import Response

# Create your views here.



class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

class RegisterListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        django_logout(request)
        return Response(status=204)

class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

    def post_create(self,serializer):
        serializer.save(author=self.request.user)
   
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
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    def post_update(self,serializer):
        serializer.save(author=self.request.user)


    
    
"""class PostViewSet(viewsets.ViewSet):
    

    def list(self,request):
        post=Post.objects.all()
        serializer=PostSerializer(post,many=True,context={"request":request})
        response_dict={"error":False,"message":"All  List Data","data":serializer.data}
        return Response(response_dict)

    def create(self,request):
        try:
            serializer=PostSerliazer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Blog Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving Company Data"}
        return Response(dict_response)

    def retrieve(self, request, pk=None):
        queryset = Company.objects.all()
        company = get_object_or_404(queryset, pk=pk)
        serializer = PostSerliazer(post, context={"request": request})

        serializer_data = serializer.data
        # Accessing All the Medicine Details of Current Medicine ID
        

        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def update(self,request,pk=None):
        try:
            queryset=post.objects.all()
            post=get_object_or_404(queryset,pk=pk)
            serializer=postSerliazer(post,data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Successfully Updated Company Data"}
        except:
            dict_response={"error":True,"message":"Error During Updating Company Data"}

        return Response(dict_response)

post_list=PostViewSet.as_view({"get":"list"})
post_create=PostViewSet.as_view({"post":"create"})
post_update=PostViewSet.as_view({"put":"update"})"""


"""class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)"""
