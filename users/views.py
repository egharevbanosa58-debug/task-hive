from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import SignUpSerializer, ProfileSerializer

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import Profile

from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class SignupView(APIView):
    def post(self, request):
        # Getting the data from the request
        # username = request.data.get('username')
        # email = request.data.get('email')
        # password = request.data.get('password')

        # # Validating the data (Checking if username exists)
        # if User.objects.filter(username=username).exists():
        #     return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        # elif User.objects.filter(email=email).exists():
        #     return Response({'error': 'Email already Exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        # # Creating the user
        # user = User.objects.create_user(username=username, email=email)
        # user.set_password(password) # Hashs the password
        # user.save() # As ususal.... Saves the user

        # return Response({'message': 'User created Successfully'}, status=status.HTTP_201_CREATED)
    
        serializer = SignUpSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created Successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        # Ensures a profile is created
        profile, created = Profile.objects.get_or_create(user=request.user)

        serializer = ProfileSerializer(profile)

        return Response(serializer.data)
        # print(f"User: {request.user}") # Debug
        # user = request.user # The currently authenticated user
        # profile = user.profile # Access the related Profile model

        # data = {
        #     'username': user.username,
        #     'email': user.email,
        #     'role': profile.role,
        # }

        # return Response(data, status=status.HTTP_200_OK)



        # Now the PATCH method to allow editing of profile
    def patch(self, request):
        # First we get the logged in user's profile, creates if it doesnt exists
        profile, _ = Profile.objects.get_or_create(user=request.user)

        # This tells DRF the object to be modified, the new value from the request and that it does not need to send all the fields
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        
        # After the data has been modified...
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)


# The LogOut View
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({ 'message': 'Logged out Successfully' }, status=status.HTTP_200_OK)
        
        except Exception:
            return Response({ 'error': 'Invalid Token' }, status=status.HTTP_400_BAD_REQUEST)