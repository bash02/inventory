from rest_framework import serializers
from .models import IngredientTransaction, ProductTransaction, PurchasedIngredient, SoldProduct


class ProductTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTransaction
        fields = ['id', 'category', 'title', 'number_in_stock', 'darmaged']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientTransaction
        fields = ['id', 'category', 'title', 'number_in_stock', 'darmaged']

class SoldProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoldProduct
        fields = ['id', 'transaction', 'content_type', 'object_id', 'content_object']


class PurchasedIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchasedIngredient
        fields = ['id', 'transaction', 'content_type', 'object_id', 'content_object']
