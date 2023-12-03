from django.contrib import admin
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    list_display = ['title', 'number_in_stock', 'collection_title']

    def collection_title(self, product):
        return product.collection.title


@admin.register(models.ProductCollection)
class ProductCollectionAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(models.Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    list_display = ['title', 'number_in_stock', 'collection_title']

    def collection_title(self, rawmaterail):
        return rawmaterail.collection.title


@admin.register(models.IngredientCollection)
class IngredientCollectionAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
