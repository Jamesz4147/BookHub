from django.urls import path, include
from .views import *

urlpatterns = [
    path('', register, name='register'),
    path('login', UserLoginView.as_view(), name='login')
]
