from django.shortcuts import render
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from .models import Multik
from .serializeer import HomeSRL
from rest_framework.response import Response

# Create your views here.
class RegisterView(APIView):

    @swagger_auto_schema(request_body=HomeSRL)
    def post(self, request):
        serializer = HomeSRL(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class GetView(APIView):
    def get(self, request):
        serialzier = HomeSRL(data = request.data)
        if serialzier.is_valid():
            serialzier.save()
            return Response(serialzier.data)
        else:
            return Response(serialzier.errors)

class GetOneView(APIView):
    def get(self, request, pk):
        user = Multik.objects.filter(id =pk).first()
        serializer = HomeSRL(user)
        return Response(serializer.data)


class EditView(APIView):
    @swagger_auto_schema(request_body=HomeSRL)
    def patch(self, request, pk):
        user = Multik.objects.filter(id = pk).first()
        user.name = request.data.get('name')
        serializer = HomeSRL(user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class DeleteView(APIView):

    def delete(self, request, pk):
        multik = Multik.objects.filter(id=pk).first()
        multik.delete()
        return Response("Multik o'chirildi")



















