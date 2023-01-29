from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework import status, generics, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from django.contrib.auth.models import User, Group
from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import UserSerializer, CategorySerializer, MenuItemSerializer, OrderSerializer, CartSerializer, \
    OrderItemSerializer
from datetime import date


class LittleLemonPermission(IsAdminUser):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return super().has_permission(request, view)


# Create your views here.

# 5.	Managers can log in
# 12.	Customers can log in using their username and password and get access tokens
# 11.	Customers can register
#  DONE using djoser

# 1.	The admin can assign users to the manager group
# 2.	You can access the manager group with an admin token
@api_view(['GET', 'POST'])
@permission_classes([LittleLemonPermission])
def manager_user(request):
    if request.method == 'GET':
        managers = User.objects.filter(groups=1)
        serializer = UserSerializer(managers, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        username = request.data['username']

        if username:
            manager_role = Group.objects.get(name="Manager")
            user = get_object_or_404(User, username=username)
            manager_role.user_set.add(user)
            return Response({"message": "User assigned to manager group"}, status.HTTP_201_CREATED)
        return Response({"message": "Username not found"}, status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response('test manager user')


# 6.	Managers can update the item of the day
@api_view(['GET', 'PATCH', 'PUT'])
@permission_classes([IsAuthenticated])
def update_item(request, pk):
    try:
        item = MenuItem.objects.get(pk=pk)

        if request.method == 'GET':

            serializer = MenuItemSerializer(item).data
            return JsonResponse(serializer, safe=False)

        elif request.user.groups.filter(name='Manager').exists():

            serializer = MenuItemSerializer(item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Successfully updated item of the day!"}, status.HTTP_200_OK)
            return Response({"message": "Data not valid"}, status.HTTP_400_BAD_REQUEST)

    except ObjectDoesNotExist:
        return Response({"message": "Data not existing"}, status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e, status.HTTP_500_INTERNAL_SERVER_ERROR)


# 9.	The delivery crew can access orders assigned to them -> GET for Delivery Crew
# 20.	Customers can place orders -> POST
# 21.	Customers can browse their own orders -> GET
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def orders_items(request):
    try:
        user = request.user
        if request.method == 'GET':
            if request.user.groups.filter(name='Delivery Crew').exists():
                order = Order.objects.get(delivery_crew=user)
            else:
                order = Order.objects.get(user=user)
            serializer = OrderSerializer(order, context={'request': request})
            return Response(serializer.data, status.HTTP_200_OK)

        elif request.method == 'POST':
            cart = Cart.objects.get(user=user)
            menu_item = cart.menuitem
            quantity = cart.quantity
            unit_price = cart.unit_price
            price = cart.price

            OrderItem.objects.create(
                order=user,
                menuitem=menu_item,
                quantity=quantity,
                unit_price=unit_price,
                price=price
            )

            Order.objects.create(
                user=user,
                total=price,
                date=date.today()
            )
            return Response({"message": "Successfully created order!"}, status.HTTP_201_CREATED)

    except ObjectDoesNotExist:
        return Response({"message": "Data not exist"}, status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return Response(e)


# 7.	Managers can assign users to the delivery crew
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def delivery_crew(request):
    try:
        if request.method == 'GET':
            managers = User.objects.filter(groups=2)
            serializer = UserSerializer(managers, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        elif request.method == 'POST':
            username = request.data['username']

            if username:
                delivery_role = Group.objects.get(name="Delivery Crew")
                user = get_object_or_404(User, username=username)
                delivery_role.user_set.add(user)
                return Response({"message": "User assigned to Delivery Crew group"}, status.HTTP_201_CREATED)

        return Response({"message": "Username not found"}, status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return Response(e, status.HTTP_500_INTERNAL_SERVER_ERROR)


# 8.	Managers can assign orders to the delivery crew
# 10.	The delivery crew can update an order as delivered

def update_delivery_crew_order(request, pk):

    try:
        if request.user.groups.filter(name='Delivery Crew' or 'Manager').exists():
            order = Order.objects.get(pk=pk)

            serializer = OrderSerializer(order, data=request.data, context={'request': request}, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Successfully updated the order!"}, status.HTTP_201_CREATED)
            else:
                return Response({"message": "data not valid"}, status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return Response(e)


# 4.	The admin can add categories
# 13.	Customers can browse all categories
class CategoriesView(generics.ListCreateAPIView):
    permission_classes = [LittleLemonPermission]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# 3.	The admin can add menu items
# 14.	Customers can browse all the menu items at once
# 15.	Customers can browse menu items by category
# 16.	Customers can paginate menu items
# 17.	Customers can sort menu items by price
class MenuItemView(generics.ListCreateAPIView):
    permission_classes = [LittleLemonPermission]
    serializer_class = MenuItemSerializer
    ordering_fields = ['price']

    param_check_list = ['category']

    def get_queryset(self):
        queryset = MenuItem.objects.all()

        params = self.check_for_params()
        filtered = {k: v for k, v in params.items() if v}
        return queryset.filter(**filtered)

    def check_for_params(self) -> dict:
        if not self.param_check_list:
            return {}
        else:
            param_dict = {}
            for p in self.param_check_list:
                param_dict[p] = self.request.query_params.get(p, None)
            return param_dict


# 18.	Customers can add menu items to the cart
# 19.	Customers can access previously added items in the cart
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def cart_items(request):
    try:
        user = request.user
        if request.method == 'GET':
            cart = Cart.objects.get(user=user)
            serializer = CartSerializer(cart)
            return Response(serializer.data, status.HTTP_200_OK)
        elif request.method == 'POST':
            name = request.data['menuitem']
            quantity = int(request.data['quantity'])

            menuitem = MenuItem.objects.get(title=name)
            unit_price = menuitem.price
            cart_items = Cart.objects.create(
                user=user,
                menuitem=menuitem,
                quantity=quantity,
                unit_price=unit_price,
                price=quantity * unit_price
            )
            cart = CartSerializer(cart_items, data=cart_items)
            if cart.is_valid():
                cart.save(cart_items)
            return Response({"message": "Successfully updated cart!"}, status.HTTP_201_CREATED)

    except Exception as e:
        return Response(e)
