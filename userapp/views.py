from django.shortcuts import render
import json 
from app.models import Product,Cart,User,Order
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.db.models import Sum

# Create your views here.

def landing(request):
    if request.session:
       
        products_first_ten =Product.objects.all()[:10]
        with open("files/products.json", "r") as read_file:
            data = json.load(read_file)
        for product_data in data['product_details']:
            product = Product.objects.update_or_create(**product_data)
        product_from_json = data['product_details']
        context = {
            'products_first_ten' : products_first_ten,
            'product_from_json' : product_from_json
        }
        print(context)
        # try:
        #     cart_count = Cart.objects.filter(user_id = User.objects.get(id=request.session.get('user_id')))
        #     print(cart_count)
        #     request.session['cart_count']=cart_count
        # except Exception as e:
        #     print("::::::::::::::::::::::::::::::::e",e)
        return render(request,'index.html',context)
   


   

def singlepage(request,product_id):
    product_single = Product.objects.get(product_id=product_id)
    context = {
        'product_single' : product_single,
    }
    return render(request,'single.html',context)


@csrf_exempt
def add_cart(request):
  
    data_set={}
    try:
        userId = request.POST['user_id']
        productId = request.POST['product_id']
        quantity = request.POST['quantity']
        price = request.POST['price']
        # print(userId,productId,quantity, price)
        total_price = int(quantity)*float(price)
        # print(total_price)
        obj,cart = Cart.objects.update_or_create(user_id=User.objects.get(id=userId),
                                    product_id=Product.objects.get(product_id=productId),
                                    product_count=int(quantity),tottal_price=total_price,status=True)
        # print(obj)
        cart_count = Cart.objects.filter(user_id=User.objects.get(id=userId)).count()
        # print(cart_count)
        data_set['cart_count']=cart_count
        data_set['status']= True
    except Exception as e:
        print("EX::::",e)
        data_set['cart_count']=0
        data_set['status']= False
      
    return HttpResponse(json.dumps(data_set), content_type="application/json")


def checkout(request,user_id):
    orders = Cart.objects.filter(status =True ,user_id = User.objects.get(id=user_id))
    print('orders',orders)
    product_total_amount = Cart.objects.filter(user_id = User.objects.get(id=user_id),status=True).aggregate(total_price=Sum('tottal_price'))
    print(product_total_amount)
    if product_total_amount['total_price'] == None:
        total_amount = 0
    else:
        total_amount = product_total_amount['total_price']
    
    context={
        'orders':orders,
        'total_amount':total_amount,
        'user_id':user_id
    }
   
    return render(request,'checkout.html',context)


@csrf_exempt    
def cartdelete(request):
    cartid =request.POST['cart_id']
    print(type(cartid))
    cart_obj = Cart.objects.filter(id =int(cartid))
    print(cart_obj)
    cart_obj.update(status = False)
    product_total_amount = Cart.objects.filter(user_id = User.objects.get(id=user_id),status=True).aggregate(total_price=Sum('tottal_price'))
    print(product_total_amount)
    if product_total_amount['total_price'] == None:
        total_amount = 0
    else:
        total_amount = product_total_amount['total_price']
    
    data_set={
        'status':True,
        'total_amount':total_amount
    }
    return HttpResponse(json.dumps(data_set),content_type="application/json")
@csrf_exempt    
def placeorder(request):
    userid =request.POST['user_id']
    total_amount =request.POST['total_amount']
    # print("llllllllllllllllllllllll",total_amount)
    obj,order = Order.objects.update_or_create(user_id=User.objects.get(id=userid),is_paid = True,order_status = True,total_amount=total_amount)
    # print(obj)
   
    data_set={
        'status':True
    }
    return HttpResponse(json.dumps(data_set),content_type="application/json") 

def invoice(request,userid):
    print("ljkkl")
    order = Order.objects.filter(user_id=User.objects.get(id=userid),is_paid = True,order_status = True).first()
    print("----------------------",order.total_amount)
    cart=Cart.objects.filter(user_id=User.objects.get(id=userid),status=True)
    print("-----------------------------",cart)
    invoice_id ="ORD"+str(userid)
    context = {
        'order':order,
        'cart' :cart,
        'user_id':userid,
        'invoice_id':invoice_id
    }
    return render(request,'invoice.html',context)
    


