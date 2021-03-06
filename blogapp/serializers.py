from rest_framework import serializers
from rest_framework import exceptions
from blogapp.models import Post
from django.contrib.auth import get_user_model

from django.contrib.auth import authenticate
from rest_framework.serializers import SerializerMethodField
    
from rest_framework.serializers import (
    CharField)

    

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            
        ]




class RegistrationSerializer(serializers.ModelSerializer):

	password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = User
		fields = ['email', 'username', 'password', 'password2']
		extra_kwargs = {
				'password': {'write_only': True},
		}	

    


	def	save(self):

		user = User(
					email=self.validated_data['email'],
					username=self.validated_data['username']
				)
		password = self.validated_data['password']
		password2 = self.validated_data['password2']
		if password != password2:
			raise serializers.ValidationError({'password': 'Passwords must match.'})
		user.set_password(password)
		user.save()
		return user



     

class LoginSerializer(serializers.Serializer):
    token = CharField(allow_blank=True, read_only=True)
    username = serializers.CharField()
    password = serializers.CharField()
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'token',
            
        ]

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "User is deactivated."
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to login with given credentials."
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide username and password both."
            raise exceptions.ValidationError(msg)
        return data

class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'image',
            'content',
            'publish']

class PostSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    class Meta:
        model=Post
        fields=[
            'id',
            'user',
            'title',
            'content',
            'publish']
    def get_user(self,obj):
        return str(obj.user.username)