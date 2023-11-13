from django.urls import path
from .views import *
from userapp import views


urlpatterns = [
        path('landing', views.landing,name='landing'),
        path('singlepage/<int:product_id>', views.singlepage,name='singlepage'),
        path('add_cart',views.add_cart,name='add_cart'),
        path('checkout/<int:user_id>', views.checkout,name='checkout'),
        path('cartdelete', views.cartdelete,name='cartdelete'),
        path('placeorder',views.placeorder,name='placeorder'),
        path('invoice/<int:userid>',views.invoice,name='invoice')
       
]