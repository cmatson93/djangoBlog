from django.urls import path 
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # path('help', views.post_help, name='help'),
    path('<slug:slug>/', views.post_detail , name='detail')
]
