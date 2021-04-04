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
    first_name = models.CharField("Nome", max_length=30)
    last_name = models.CharField("Sobrenome", max_length=140)
    created = models.DateTimeField("Data de criação", auto_now_add=True)
    updated = models.DateTimeField("Data de modificação", auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField("Usuário ativo", default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ['-created']

    def __str__(self):
        role_verbose = self.ROLES[self.role][1]
        return f'[{role_verbose}] {self.first_name} {self.last_name}'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name
