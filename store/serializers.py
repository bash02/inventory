from rest_framework import serializers
from .models import Product, ProductCollection, Ingredient, IngredientCollection


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'collection', 'title', 'number_in_stock', 'darmaged']


class ProductCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCollection
        fields = ['id', 'title']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'collection', 'title', 'number_in_stock', 'darmaged']


class IngredientCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientCollection
        fields = ['id', 'title']
