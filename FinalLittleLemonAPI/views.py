from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response


# Create your views here.

# 1.	The admin can assign users to the manager group
# 2.	You can access the manager group with an admin token
@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def manager_user(request):
    return Response('assign_user_to_manager')


# 3.	The admin can add menu items
def add_menu_item(request):
    return Response('add_menu_item')


# 4.	The admin can add categories
def add_menu_category(request):
    return Response('add_menu_category')


# 5.	Managers can log in
# 12.	Customers can log in using their username and password and get access tokens
def login(request):
    return Response('login')


# 6.	Managers can update the item of the day
def update_item(request):
    return Response('update_item')


# 7.	Managers can assign users to the delivery crew
def assign_user_to_delivery_crew(request):
    return Response('assign_user_to_delivery_crew')


# 8.	Managers can assign orders to the delivery crew
def assign_order_to_delivery_crew(request):
    return Response('assign_order_to_delivery_crew')


# 9.	The delivery crew can access orders assigned to them
def get_delivery_crew_order(request):
    return Response('get_delivery_crew_order')


# 10.	The delivery crew can update an order as delivered
def update_delivery_crew_order(request):
    return Response('update_delivery_crew_order')


# 11.	Customers can register
def register_customer(request):
    return Response('register_customer')


# 13.	Customers can browse all categories
def get_categories(request):
    return Response('get_categories')


# 14.	Customers can browse all the menu items at once
# 15.	Customers can browse menu items by category
# 16.	Customers can paginate menu items
# 17.	Customers can sort menu items by price
def get_menu_items(request):
    return Response('get_menu_items')


# 18.	Customers can add menu items to the cart
def add_menu_item_to_cart(request):
    return Response('add_menu_item_to_cart')


# 19.	Customers can access previously added items in the cart
def get_menu_item_to_cart(request):
    return Response('get_menu_item_to_cart')


# 20.	Customers can place orders
def place_order(request):
    return Response('place_order')


# 21.	Customers can browse their own orders
def get_customer_orders(request):
    return Response('get_customer_orders')
