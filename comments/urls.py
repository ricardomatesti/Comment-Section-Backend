from django.urls import path

from comments.models import Reply
from .views import (
    UserDetail,
    UserListCreate,
    CommentListCreate,
    CommentDetail,
    ReplyDetail,
    ReplyListCreate,
)

urlpatterns = [
    path("user/", UserListCreate.as_view(), name="user-list"),
    path("user/<int:pk>/", UserDetail.as_view(), name="user-detail"),
    path("comment/", CommentListCreate.as_view(), name="comment-list"),
    path("comment/<int:pk>/", CommentDetail.as_view(), name="comment-detail"),
    path("reply/", ReplyListCreate.as_view(), name="reply-list"),
    path("reply/<int:pk>/", ReplyDetail.as_view(), name="reply-detail"),
]
