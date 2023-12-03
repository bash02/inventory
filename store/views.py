from rest_framework.viewsets import ModelViewSet
from .models import Product, ProductCollection, Ingredient, IngredientCollection
from .serializers import ProductSerializer, ProductCollectionSerializer, IngredientSerializer, IngredientCollectionSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class IngredientViewSet(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class ProductCollectionViewSet(ModelViewSet):
    queryset = ProductCollection.objects.all()
    serializer_class = ProductCollectionSerializer


class IngredientCollectionViewSet(ModelViewSet):
    queryset = IngredientCollection.objects.all()
    serializer_class = IngredientCollectionSerializer