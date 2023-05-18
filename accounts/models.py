# accoutns/models.py

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from posts.models import Review, Gallery, Artist, Exhibition


class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        nickname = self.model(nickname=nickname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password):
        user = self.create_user(
            email=email,
            nickname=nickname,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    # required fileds
    profile_image = models.ImageField(
        blank=True, null=True, upload_to='images/profile/')
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=20)
    password = models.CharField(max_length=128)

    # MTM fields

    followings = models.ManyToManyField(
        'self', related_name='followers', symmetrical=False)
    like_exhibitions = models.ManyToManyField(
        Exhibition, related_name='like_users')
    like_reviews = models.ManyToManyField(Review, related_name="like_users")

    # status field

    is_artist = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
