from django.db import models


class BaseProductModel(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    price = models.PositiveIntegerField(verbose_name='Цена')

    # class Meta:
    #     abstract = True


class PC(BaseProductModel):

    CP = models.CharField(max_length=150, verbose_name='Процессор')
    OZU = models.PositiveIntegerField(verbose_name='ОЗУ', help_text='(Объем)')
    memory = models.PositiveIntegerField(verbose_name='ПЗУ', help_text='(Объем)')
    video_card = models.CharField(max_length=200, verbose_name='Видеокарта')
    power_block = models.CharField(max_length=200, verbose_name='Блок питания')
    mother_bord = models.CharField(max_length=200, verbose_name='Материнская плата')

    def __str__(self):
        return self.name


class MobilePhone(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    price = models.PositiveIntegerField(verbose_name='Цена')

    CP = models.CharField(max_length=150, verbose_name='Процессор')
    OZU = models.PositiveIntegerField(verbose_name='ОЗУ', help_text='(Объем)')
    memory = models.PositiveIntegerField(verbose_name='ПЗУ', help_text='(Объем)')
    battery = models.PositiveIntegerField(verbose_name='Батарея', help_text='mAh')
    display = models.CharField(max_length=200, verbose_name='Экран')

    def __str__(self):
        return self.name


class TV(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    price = models.PositiveIntegerField(verbose_name='Цена')

    display = models.CharField(max_length=200, verbose_name='Экран')

    def __str__(self):
        return self.name