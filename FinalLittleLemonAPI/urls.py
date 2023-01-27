from django.urls import path
from . import views

urlpatterns = [
    path('group/manager/users', views.manager_user),
]