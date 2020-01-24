# Generated by Django 3.0.2 on 2020-01-24 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_product', models.CharField(choices=[('PC', 'PC'), ('MobilePhone', 'Mobile phone'), ('TV', 'TV')], default='PC', max_length=150)),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='TVCharacters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display', models.CharField(max_length=200, verbose_name='Экран')),
                ('img', models.ImageField(default='phone.png', upload_to='Products/PC')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='PCCharacters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CP', models.CharField(max_length=150, verbose_name='Процессор')),
                ('OZU', models.PositiveIntegerField(help_text='(Объем)', verbose_name='ОЗУ')),
                ('memory', models.PositiveIntegerField(help_text='(Объем)', verbose_name='ПЗУ')),
                ('video_card', models.CharField(max_length=200, verbose_name='Видеокарта')),
                ('power_block', models.CharField(max_length=200, verbose_name='Блок питания')),
                ('mother_bord', models.CharField(max_length=200, verbose_name='Материнская плата')),
                ('img', models.ImageField(default='phone.png', upload_to='Products/PC')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='MobilePhoneCharacters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CP', models.CharField(max_length=150, verbose_name='Процессор')),
                ('OZU', models.PositiveIntegerField(help_text='(Объем)', verbose_name='ОЗУ')),
                ('memory', models.PositiveIntegerField(help_text='(Объем)', verbose_name='ПЗУ')),
                ('battery', models.PositiveIntegerField(help_text='mAh', verbose_name='Батарея')),
                ('display', models.CharField(max_length=200, verbose_name='Экран')),
                ('img', models.ImageField(default='phone.png', upload_to='Products/PC')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]