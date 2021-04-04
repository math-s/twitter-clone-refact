from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from accounts.managers import CustomUserManager


class User(AbstractBaseUser):
    image = models.ForeignKey("assets.Image",
                              on_delete=models.CASCADE,
                              null=True)
    email = models.EmailField("email",
                              max_length=140,
                              unique=True)
    email_verified = models.BooleanField(default=False)
    phone = models.CharField("Contato", max_length=14)
    name = models.CharField("Nome", max_length=60)
    nick = models.CharField("Nome", max_length=20)
    created = models.DateTimeField("Data de criação", auto_now_add=True)
    updated = models.DateTimeField("Data de modificação", auto_now=True)
    followers = models.ManyToManyField("accounts.User")

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ['-created']

    def get_full_name(self):
        return f'{self.name} {self.nick}'

    def get_short_name(self):
        return self.nick
