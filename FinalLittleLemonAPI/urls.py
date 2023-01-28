from django.urls import path
from . import views

urlpatterns = [
    path('group/manager/users', views.manager_user),
    path('categories', views.CategoriesView.as_view()),
    path('menu-items', views.MenuItemView.as_view()),
    path('menu-items/<int:pk>', views.update_item),
    path('group/delivery-crew/users', views.delivery_crew),
]