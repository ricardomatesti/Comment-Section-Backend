from django.urls import path

from .views import (
    UserListCreate,
    CommentListCreate,
    CommentDetail,
    ReplyDetail,
    ReplyListCreate,
)

urlpatterns = [
    path("user/", UserListCreate.as_view(), name="user-list"),
    path("comment/", CommentListCreate.as_view(), name="comment-list"),
    path("comment/<int:pk>/", CommentDetail.as_view(), name="comment-detail"),
    path("reply/", ReplyListCreate.as_view(), name="reply-list"),
    path("reply/<int:pk>/", ReplyDetail.as_view(), name="reply-detail"),
]
