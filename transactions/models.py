from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class IngredientTransaction(models.Model):
    quantity = models.IntegerField()
    unit_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(1)])
    date = models.DateTimeField(auto_now=True)


class ProductTransaction(models.Model):
    quantity = models.IntegerField()
    unit_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(1)])
    date = models.DateTimeField(auto_now=True)

class SoldProduct(models.Model):
    transaction = models.ForeignKey(ProductTransaction, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.IntegerField()
    content_object = GenericForeignKey

class PurchasedIngredient(models.Model):
    transaction = models.ForeignKey(IngredientTransaction, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.IntegerField()
    content_object = GenericForeignKey 