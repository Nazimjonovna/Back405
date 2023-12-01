from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from .models import *
from .serializer import *

# Create your views here.
class RegisterView(APIView):

    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        serializers = UserSerializer(data = request.data)
        if serializers.is_valid():
            user = serializers.save()
            access = AccessToken.for_user(user)
            refresh = RefreshToken.for_user(user)
            return Response({
                "user":serializers.data,
                'access':str(access),
                'refresh':str(refresh)
            })
        else:
            return Response(serializers.errors)


class LoginView(APIView):

    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username =username, password = password).first()
        if user:
            serializer = LoginSerializer(user)
            access = AccessToken.for_user(user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'user':serializer.data,
                'access':str(access),
                'refresh':str(refresh)
            })
        else:
            return Response("Siz ro'yhatdan o'tmagansz")


class EditUserView(APIView):

    @swagger_auto_schema(request_body=EditSerializer)
    def patch(self, request, pk):
        user = User.objects.filter(id = pk).first()
        if user:
            user.email = request.data.get("email")
            user.save()
            serializers = EditSerializer(user, partial=True)
            # if serializers.is_valid():
            #     serializers.save()
            #     return Response(serializers.data)
            return Response(serializers.data)
        else:
            return Response("Bunday user yo")


class DeleteView(APIView):

    def get(self, request, pk):
        user = User.objects.filter(id =pk).first()
        if user:
            user.delete()
            return Response("Malades o'chdi")
        else:
            return Response("Bunday user yo")


class OrderView(APIView):
    permission_classes = [IsAuthenticated,]

    @swagger_auto_schema(request_body=OrderSerializer)
    def post(self, request):
        serializers = OrderSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)










