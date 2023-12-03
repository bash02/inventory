from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('', views.ProductViewSet, basename='products')
router.register('ingredients', views.IngredientViewSet, basename='ingredients')
router.register('productcollections', views.ProductCollectionViewSet, basename='product-collections')
router.register('ingredientcollections', views.IngredientCollectionViewSet, basename='ingredient-collections')

urlpatterns = router.urls