from django.db import models
from user.models import User


class Album(models.Model):
    """This model holds information about user created albums"""

    class Status(models.TextChoices):
        """Status of the album"""
        PUBLIC = 'public', 'Public'
        PRIVATE = 'private', 'Private'

    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='images/')
    status = models.CharField(max_length=7, default=Status.PUBLIC)
    upload_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['name'], name='name_idx'),
            models.Index(fields=['user'], name='user_idx'),
        ]

        # The name and user must be unique together
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'user'], name='unique_name_user'),
        ]
