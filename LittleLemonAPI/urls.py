from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('books', views.BookView.as_view()),
    path('books/<int:pk>', views.SingleBookView.as_view()),
    path('menu-items', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('categories', views.CategoriesView.as_view()),
    path('secret', views.secret),
    path('api-token-auth', obtain_auth_token),
    path('me', views.me),
    path('manager-view', views.manager_view),
    path('guess-throttle', views.throttle_check_anon),
    path('user-throttle', views.throttle_check_user),
    path('group/manager/users', views.manager_permission),
    path('ratings', views.RatingsView.as_view()),
]
