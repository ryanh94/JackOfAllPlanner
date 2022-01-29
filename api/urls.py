import imp
from django.urls import path, include
from . import user_view

urlpatterns = [
    path('users/<int:id>', user_view.getUser),
    path('users/add', user_view.createUser)
]