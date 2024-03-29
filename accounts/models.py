from django.contrib.auth.models import User as AuthUser, PermissionsMixin
from django.db import models
from django.utils import timezone


class User(AuthUser, PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)
