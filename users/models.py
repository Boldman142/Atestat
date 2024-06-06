from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    phone = PhoneNumberField(max_length=100, verbose_name='Номер телефона', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    image = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
