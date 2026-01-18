from django.shortcuts import render
from rest_framework import generics
from .models import User, Comment, Reply
from .serializers import UserSerializer, CommentSerializer, ReplySerializer


# Vista para Users: permite Ver todos y Crear nuevos
class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Vista para borrar o editar un User específico
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Vista para Comments: permite Ver todos y Crear nuevos
class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# Vista para borrar o editar un comment específico
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# Vista para Reply: permite Ver todos y Crear nuevos
class ReplyListCreate(generics.ListCreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer


# Vista para borrar o editar un reply específico
class ReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
