from rest_framework import serializers
from .models import User, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"  # O una lista: ['id', 'titulo', 'imagen']


class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source="user.name")

    class Meta:
        model = Comment
        fields = ["id", "user", "user_name", "text", "date"]


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
