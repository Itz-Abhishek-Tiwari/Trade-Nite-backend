from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializer import LoginSerializer, ResgisterSerializer, TestSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import Test
from rest_framework.permissions import IsAuthenticated


class LoginView(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if not serializer.is_valid():
            return Response(
                {"message": serializer.errors, "status": status.HTTP_409_CONFLICT}
            )

        username = serializer.data["username"]
        password = serializer.data["password"]
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response(
                {"refresh": str(refresh), "access": str(refresh.access_token)},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"message": "Invalid credentials"}, status=status.HTTP_404_NOT_FOUND
        )


class ResgisterView(APIView):
    def post(self, request):
        data = request.data
        serializer = ResgisterSerializer(data=data)

        if not serializer.is_valid():
            return Response(
                {
                    "message": serializer.errors,
                    "status": status.HTTP_400_BAD_REQUEST,
                }
            )

        serializer.save()
        return Response(
            {
                "message": "You have created a account",
            },
            status=status.HTTP_201_CREATED,
        )


class TestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        test = Test.objects.all()
        serializer = TestSerializer(test, many=True)

        return Response(
            {"data": serializer.data},
            status=status.HTTP_200_OK,
        )
