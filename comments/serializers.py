from rest_framework import serializers
from .models import Reply, User, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"  # O una lista: ['id', 'titulo', 'imagen']


class ReplySerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source="user.name")
    user_photo_url = serializers.ReadOnlyField(source="user.photo_url")
    comment = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all())

    class Meta:
        model = Reply
        fields = [
            "id",
            "user",
            "user_name",
            "user_photo_url",
            "text",
            "date",
            "comment",
            "votes",
        ]


class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source="user.name")
    user_photo_url = serializers.ReadOnlyField(source="user.photo_url")
    replies = ReplySerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "user",
            "user_name",
            "user_photo_url",
            "text",
            "date",
            "replies",
            "votes",
        ]
