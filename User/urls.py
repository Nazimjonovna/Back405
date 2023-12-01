from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('order/', OrderView.as_view()),
    path('edit/', EditUserView.as_view()),
    path('delete/', DeleteView.as_view()),
]