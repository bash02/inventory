from django.db import models


class ProductCollection(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']

class Product(models.Model):
    collection = models.ForeignKey(ProductCollection, on_delete=models.CASCADE, related_name='products', null=True)
    title = models.CharField(max_length=255)
    number_in_stock = models.IntegerField()
    darmaged = models.IntegerField()

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']


class IngredientCollection(models.Model):
    title  = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['title']


class Ingredient(models.Model):
    collection = models.ForeignKey(IngredientCollection, on_delete=models.CASCADE, related_name='ingredients', null=True)
    title = models.CharField(max_length=255)
    number_in_stock = models.IntegerField()
    darmaged = models.IntegerField()

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['title']


