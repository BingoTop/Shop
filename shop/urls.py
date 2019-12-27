from django.urls import path
from .views import product_detail
from .views import product_in_category


urlpatterns = [
    path('',product_in_category, name= 'product_all'),
    path('<slug:category_slug>')

]
