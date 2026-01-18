from django.db import models, migrations


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    photo_url = models.URLField(max_length=500, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class Reply(models.Model):
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name="reply",
    )
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
