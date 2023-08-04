from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class User(AbstractUser):
    """This model holds basic information for users of the application"""

    slug = models.SlugField()

    def __str__(self) -> str:
        return self.username

    def get_absolute_url(self):
        return reverse("user:profile", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        """Used to auto fill the slug field with the username"""
        self.slug = slugify(self.username)
        return super(User, self).save(*args, **kwargs)

    class Meta:
        # Indexes for query optimization
        indexes = [
            models.Index(fields=["username"], name="username_idx"),
            models.Index(fields=["email"], name="email_idx"),
        ]
