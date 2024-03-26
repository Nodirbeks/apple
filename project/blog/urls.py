from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/', category_page, name='category'),
    path('article/<int:article_id>/', article_detail, name='article'),
    path('add_article/', add_article, name='add_article'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('search/', search_results, name='search'),
    path('delete/<int:id>/', delete_article, name='delete')
]
