from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

# Serializer goes here

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        extra_kwargs = {
            'password':  {'write_only': True}
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('This email already exists')
        
        return value

    # The create() function should have only one arguement -- validated_date
    def create(self, validated_data): 
        
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        return user
    

class ProfileSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')

    class Meta:
        model = Profile
        fields = ['id', 'username', 'email', 'role']