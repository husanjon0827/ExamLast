from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models


class SoftDeleteUserManager(UserManager):
    def soft_delete(self, user_id):
        user = self.get(pk=user_id)
        if user:
            user.is_active = False
            user.save()


class User(AbstractUser):
    is_active = models.BooleanField(default=True)
    objects = SoftDeleteUserManager()
