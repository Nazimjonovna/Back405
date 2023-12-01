from django.urls import path
from .views import *

urlpatterns = [
    path('post/', RegisterView.as_view()),
    path('get/', GetView.as_view()),
    path('one/<int:pk>/', GetOneView.as_view()),
    path('edit/<int:pk>/', EditView.as_view()),
    path('delete/<int:pk>/', DeleteView.as_view()),
]



# asosiy urlga qo'shish kk
# data qo'shib ishlatish kk