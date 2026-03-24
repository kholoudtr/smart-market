from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Category , Product , Cart
import random
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    categories = Category.objects.all()
    random_products = []

    for category in categories:
        products_in_category = list(Product.objects.filter(category=category))
        if products_in_category:  # تأكد من أن هناك منتجات في الفئة
            chosen_product = random.choice(products_in_category)
            random_products.append(chosen_product)

    random.shuffle(random_products)
    return render(request, 'index.html', {'products': random_products})

@login_required
def category(request):
      category=Category.objects.all()
      product=Product.objects.all()
      return render(request,'category.html',{'category':category})

@login_required
def product(request,id):
      category=get_object_or_404(Category,id=id)
      products = category.product_set.all()
      print(product)
      return render(request,'product.html',{'category':category , 'products':products})


@login_required
def cart(request,id):
      if id:
            product=get_object_or_404(Product,id=id)
            cart_item,created=Cart.objects.get_or_create(user=request.user,product=product)
            if not created:
                  cart_item.quantity+=1
                  cart_item.save()
      cart_item=Cart.objects.filter(user=request.user) 
      total_price=sum (item.product.price * item.quantity for item in cart_item)
      return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})
