from django.db import models
from datetime import date

"""
Создайте три модели Django: клиент, товар и заказ. Клиент
может иметь несколько заказов. Заказ может содержать
несколько товаров. Товар может входить в несколько
заказов.
Поля модели "Клиент":
○ имя клиента
○ электронная почта клиента
○ номер телефона клиента
○ адрес клиента
○ дата регистрации клиента

Задание №8
Поля модели "Товар":
○ название товара
○ описание товара
○ цена товара
○ количество товара
○ дата добавления товара

Поля модели "Заказ":
○ связь с моделью "Клиент", указывает на клиента,
сделавшего заказ
○ связь с моделью "Товар", указывает на товары,
входящие в заказ
○ общая сумма заказа
○ дата оформления заказа


*Допишите несколько функций CRUD для работы с
моделями по желанию. Что по вашему мнению актуально в
такой базе данных.
"""

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    registered_date = models.DateField(blank=True, null=True)
    def __str__(self):
        return f'Client_name = {self.name} Email = {self.email} phone = {self.phone} Address = {self.address} registered_date = {self.registered_date}'

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    added_date = models.DateField(blank=True, null=True, default=date.today())

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_cost = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateField(auto_now=True)

