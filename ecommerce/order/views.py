
# Create your views here.
from django.shortcuts import render
from .models import *
from django.db.models import Sum, Count
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import boto3
from django.contrib.humanize.templatetags.humanize import intcomma
# import logging
from logging.handlers import RotatingFileHandler
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render
import random
from django.conf import settings

import socket
from django.contrib import messages  


from django.db.models.functions import TruncSecond



@login_required
def home(request):
    return redirect('product_list')

@login_required
def logout_view(request):
    print("logout")
    logout(request)
    return redirect('login')






def product_detail(request, product_id):
    return redirect('product_list')

def product_basket(request, product_id):
    return redirect('product_list')

# def product_order(request, product_id):
#     return redirect('product_list')

from django.shortcuts import get_object_or_404, redirect, render
from datetime import date
import random
# from .models import Product, Order

def get_user_orders(user):
    if user.username == 'AWS01':
        OrderModel = Order01  
    elif user.username == 'AWS02':
        OrderModel = Order02  
    elif user.username == 'AWS03':
        OrderModel = Order03  
    elif user.username == 'AWS04':
        OrderModel = Order04  
    elif user.username == 'AWS05':
        OrderModel = Order05  
    elif user.username == 'AWS06':
        OrderModel = Order06  
    elif user.username == 'AWS07':
        OrderModel = Order07  
    elif user.username == 'AWS08':
        OrderModel = Order08  
    elif user.username == 'AWS09':
        OrderModel = Order09  
    elif user.username == 'AWS10':
        OrderModel = Order10  
    elif user.username == 'AWS11':
        OrderModel = Order11  
    elif user.username == 'AWS12':
        OrderModel = Order12  
    elif user.username == 'AWS13':
        OrderModel = Order13  
    elif user.username == 'AWS14':
        OrderModel = Order14  
    elif user.username == 'AWS15':
        OrderModel = Order15  
    elif user.username == 'AWS16':
        OrderModel = Order16  
    elif user.username == 'AWS17':
        OrderModel = Order17  
    elif user.username == 'AWS18':
        OrderModel = Order18  
    elif user.username == 'AWS19':
        OrderModel = Order19  
    elif user.username == 'AWS20':
        OrderModel = Order20  
    else:
        # 기본값으로 Order 모델을 사용하거나 다른 처리를 수행할 수 있습니다.
        OrderModel = Order

    return OrderModel


def product_order(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'GET':
        order_cnt = random.choice([1,2,3,4])
        promo = ['','PROMO001','PROMO002','PROMO003','PROMO004','PROMO005']
        promo_w = [70,15,8,4,2,1]
        promo_id = random.choices(promo, promo_w)[0]
        order_dt = date.today().strftime('%Y%m%d')
        order_price = product.price * int(order_cnt)
        
        # retrieve user information from the request or session
        user = request.user

        OrderModel = get_user_orders(request.user)

        try:
            # create a new order object and save to the database
            order = OrderModel.objects.create(
                cust_id=user,
                prd_id=product,
                promo_id=promo_id,
                order_cnt=order_cnt,
                order_price=order_price,
                order_dt=order_dt,
            )
            messages.success(request, '주문이 성공적으로 생성되었습니다.')  # 성공 메시지 추가
        except Exception as e:
            messages.error(request, f'주문 생성 중 오류 발생: {str(e)}')  # 에러 메시지 추가

    return redirect('product_list')



@login_required
def order_list(request):
    OrderModel = get_user_orders(request.user)
    
    orders = OrderModel.objects.annotate(
        truncated_last_update_time=TruncSecond('last_update_time')
    ).select_related('cust_id', 'prd_id').order_by('-truncated_last_update_time','id')[:50]
    
    total_order_price = orders.aggregate(Sum('order_price'))['order_price__sum'] or 0
    total_order_count = orders.aggregate(Count('id'))['id__count'] or 0
    context = {
        'orders': orders,
        'total_order_price': total_order_price,
        'total_order_count': total_order_count,
        'hostname': socket.gethostname()
    }
    
    return render(request, 'order_list.html', context)

@login_required
def customer_list(request):
    customers = User.objects.all()
    context = {'customers': customers,
               'hostname': socket.gethostname()
                }
    return render(request, 'customer_list.html', context)

@login_required
def product_list(request):

    personalize_arn = getattr(settings, 'PERSONALIZE_ARN', None)

    products = Product.objects.all()
    
    if len(personalize_arn) > 0 :
        print("personalize recommend")
        gr = get_recommendations(str(request.user.id), personalize_arn)
        recommend_ids = [ i + 1 for i in range(20 )]
        recommend_ids.reverse()
        products = sorted(products, key=lambda x: recommend_ids.index(x.id))
    else :
        print("normal recommend")

    context = {'products': products, 
               'personalize_arn':personalize_arn,
               'hostname': socket.gethostname()
               }
    return render(request, 'product_list.html', context)

def get_recommendations(user_id, personalize_arn):
    personalizeRt = boto3.client('personalize-runtime', region_name='ap-northeast-2')
    response = personalizeRt.get_recommendations(
        campaignArn=personalize_arn,
        userId=str(user_id),
        numResults=10
    )
    recommended_items = [item for item in response['itemList']]    
    return recommended_items



@login_required
def recommend_list(request):
    if request.is_ajax() and request.method == 'POST':
        # ajax POST 요청 처리
        customer_id = request.POST.get('data')
        print(customer_id)
        # 입력 데이터 처리
        recommended_items = get_recommendations(customer_id)
        
        scores = []
        recommended_products = []
        for k in recommended_items :
            recommended_products.append(Product.objects.filter(prd_id = k['itemId']))
            scores.append(k['score'])


        customer = Customer.objects.get(cust_id=customer_id)
        customer_name = customer.name

        print(recommended_products)

        recommended_product_list = []
        for i, product in enumerate(recommended_products):
            recommended_product_list.append({
                'prd_id': product[0].prd_id,
                'name': product[0].name,
                'category': product[0].category,
                'price': intcomma(product[0].price),
                'score' : scores[i]
            })
        
        data = {
            'recommended_products': recommended_product_list,
            'customer_name': customer_name
        }       

        # return JsonResponse({'recommended_products': recommended_product_list})
        return JsonResponse(data)

    # GET 요청이나 ajax가 아닌 POST 요청 처리
    return render(request, 'recommend_list.html')        


def change_order_cnt(request, product_id):

    if Order.objects.exists():
        # max_id = Order.objects.latest('id').id
        max_id = 1
        order = Order.objects.get(id=max_id)

        price = int(order.order_price / order.order_cnt)

        new_order_cnt = order.order_cnt + 1

        # print("## {} : {}".format(max_id, new_order_cnt))

        order.order_cnt = new_order_cnt
        order.order_price = price * new_order_cnt
        order.save()

    return redirect('product_list')
