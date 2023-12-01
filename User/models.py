from django.db import models
from Multik.models import Multik
from rest_framework.response import Response

# def validate_email(self, email):
#     user = User.objects.filter(email = email)
#     if user.exists():
#         return Response("Ushbu email avval ro'yhatdan o'tgan")
#     else:
#         if email.endswith('@gmail.com') or email.endswith("@mail.ru"):
#             return email
#         else:
#             return Response("Emailni noto'gri kiritdingiz")

# def validate_password(self, password):
#     if len(password) == 8:
#         return password
#     else:
#         return Response("8ta belgi kiriting")

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=8)


    def __str__(self):
        return self.username


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    multik = models.ForeignKey(Multik, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.date)





