from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .models import Book, MenuItem, Category
from .serializers import BookSerializer, MenuItemSerializer, CategorySerializer
from .pagination import SmallResultsSetPagination


class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class SingleBookView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price', 'inventory']
    filterset_fields = ['price', 'inventory']
    search_fields = ['title']
    pagination_class = SmallResultsSetPagination


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({'test secret'})


@api_view()
@permission_classes([IsAuthenticated])
def me(request):
    return Response(request.user.email)


@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    if (request.user.groups.filter(name='Manager').exists()):
        return Response({'manager view only'})
    else:
        return Response({'not allow'}, 403)


@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check_anon(request):
    return Response({'test throttle not login user'})


@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([UserRateThrottle])
def throttle_check_user(request):
    return Response({'test throttle login user'})
