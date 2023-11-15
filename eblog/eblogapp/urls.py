
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [

    path('', views.PostList.as_view(), name='home'),
    path('category/<slug:category_slug>/', views.PostList.as_view(), name='post_list_by_category'),
    path('categories/', views.CategoriesView, name='categories'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
   
]

