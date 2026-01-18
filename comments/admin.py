from django.contrib import admin
from .models import User, Comment, Reply

# Register your models here.
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Reply)
