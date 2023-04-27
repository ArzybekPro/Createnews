from django.urls import path
from . import views


urlpatterns = [
    path('',views.mini_home,name='mini_home'),
    path('create/' , views.create, name='create'),
    path('<int:pk>',views.NewsDetail,name='news_detail')
]
