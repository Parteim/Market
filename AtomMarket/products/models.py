from django.db import models
from django.utils import timezone


class Product(models.Model):
    type_list = (
        ('PC', 'PC'),
        ('MobilePhone', 'Mobile phone'),
        ('TV', 'TV'),
    )

    type_of_product = models.CharField(max_length=150, choices=type_list, default='PC')
    name = models.CharField(max_length=150, verbose_name='Название')
    price = models.PositiveIntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return str(self.name)


class PCCharacters(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE)

    CP = models.CharField(max_length=150, verbose_name='Процессор')
    OZU = models.PositiveIntegerField(verbose_name='ОЗУ', help_text='(Объем)')
    memory = models.PositiveIntegerField(verbose_name='ПЗУ', help_text='(Объем)')
    video_card = models.CharField(max_length=200, verbose_name='Видеокарта')
    power_block = models.CharField(max_length=200, verbose_name='Блок питания')
    mother_bord = models.CharField(max_length=200, verbose_name='Материнская плата')

    img = models.ImageField(upload_to='Products/PC', default='phone.png')

    def __str__(self):
        return str(self.name)


class MobilePhoneCharacters(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE)

    CP = models.CharField(max_length=150, verbose_name='Процессор')
    OZU = models.PositiveIntegerField(verbose_name='ОЗУ', help_text='(Объем)')
    memory = models.PositiveIntegerField(verbose_name='ПЗУ', help_text='(Объем)')
    battery = models.PositiveIntegerField(verbose_name='Батарея', help_text='mAh')
    display = models.CharField(max_length=200, verbose_name='Экран')

    img = models.ImageField(upload_to='Products/PC', default='phone.png')

    def __str__(self):
        return str(self.name)


class TVCharacters(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE)

    display = models.CharField(max_length=200, verbose_name='Экран')

    img = models.ImageField(upload_to='Products/PC', default='phone.png')

    def __str__(self):
        return str(self.name)