from django.db import models

from products.models import BaseProductModel


class Cart(models.Model):
    product = models.ForeignKey(BaseProductModel, on_delete=models.CASCADE)
