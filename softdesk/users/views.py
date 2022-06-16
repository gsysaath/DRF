import datetime

import jwt  # utiliser simple_jwt
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer


# Create your views here.
class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# class LoginView(APIView):
#     def post(self, request):
#         email = request.data["email"]
#         password = request.data["password"]

#         user = User.objects.filter(email=email).first()

#         if user is None:
#             raise AuthenticationFailed("User not found!")

#         if not user.check_password(password):
#             raise AuthenticationFailed("Incorrect password!")

#         payload = {
#             "id": user.id,
#             "exp": datetime.datetime.now() + datetime.timedelta(minutes=60),
#             "iat": datetime.datetime.now(),
#         }

#         token = jwt.encode(payload, "secret", algorithm="HS256")

#         response = Response()

#         response.set_cookie(key="jwt", value=token, httponly=True)
#         response.data = {"jwt": token}

#         return response


class UserView(APIView):
    def get(self, request):
        user = self.request.user
        serializer = UserSerializer(user)

        return Response(user)


# class LogoutView(APIView):
#     def post(self, request):
#         response = Response()
#         response.delete_cookie("jwt")
#         response.data = {"message": "Successfully logged out"}
#         return response
