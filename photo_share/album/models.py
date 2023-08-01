from django.db import models
from user.models import User


class Album(models.Model):
    """This model holds information about user created albums"""

    class Status(models.TextChoices):
        """Status of the album"""
        PUBLIC = 'public', 'Public'
        PRIVATE = 'private', 'Private'

    name = models.CharField(max_length=50, unique=True)
    status = models.CharField(
        max_length=7, choices=Status.choices, default=Status.PUBLIC)
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['name'], name='album_name_idx'),
            models.Index(fields=['user'], name='album_user_idx'),
        ]

        # The name and user must be unique together
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'user'], name='unique_name_user'),
        ]

        ordering = ['-creation_date']


class AlbumImage(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    upload_date = models.DateTimeField(auto_now_add=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['name'], name='album_image_name'),
        ]

        constraints = [
            models.UniqueConstraint(
                fields=['name', 'user'], name='album_image_unique_name_user')
        ]

        ordering = ['-upload_date']
