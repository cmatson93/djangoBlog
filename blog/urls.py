from django.urls import path 
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<slug:slug>/', views.post_detail , name='detail'),
    path('about/', views.about_page, name='about_page'),
]
