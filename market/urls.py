from django.urls import path
from market import views
##
urlpatterns = [
      path('index',views.index, name="index"),
      path("category",views.category, name="category"),
      path("product/<int:id>",views.product, name="product"),
      path("cart/<int:id>",views.cart, name="cart"),
      path("cart", views.view_cart, name="cart_view"),

    
]
