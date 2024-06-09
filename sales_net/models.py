from django.db import models
from users.models import User
from products.models import Product
from django.utils import timezone

# Constants
NULLABLE = {'blank': True, 'null': True}


class Levels(models.IntegerChoices):
    FACTORY = 0, 'Завод'
    RETAIL_NETWORK = 1, 'Розничная сеть'
    IP = 2, 'Индивидуальный предприниматель'


class SalesNet(models.Model):
    product = models.ManyToManyField(Product, verbose_name='Продукт')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель поставщика', **NULLABLE)
    provider = models.ForeignKey('SalesNet', on_delete=models.PROTECT, verbose_name='Поставщик', **NULLABLE)

    title = models.CharField(max_length=200, verbose_name='Название')
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    country = models.CharField(max_length=200, verbose_name='Страна')
    city = models.CharField(max_length=200, verbose_name='Город')
    street = models.CharField(max_length=200, verbose_name='Улица')
    house = models.CharField(max_length=100, verbose_name='Номер дома')

    levels = models.IntegerField(choices=Levels.choices, default=Levels.FACTORY, verbose_name='Уровень структуры')
    debt = models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Задолженность', **NULLABLE)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сеть поставки'
        verbose_name_plural = 'Сети поставки'
