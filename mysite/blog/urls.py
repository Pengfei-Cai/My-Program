#!usr/bin/pthon3
# -*- coding: UTF-8 -*-
from django.urls import path
from . import views

#start with blog
urlpatterns = [
    #id负责具体的哪篇文章，后面调用方法显示
    # #http://localhost:8000/blog/1
    path('',views.blog_list,name='blog_list'),
    path('<int:blog_id>', views.blog_details,name="详情"),
    path('type/<int:blog_type_id>',views.blogs_with_type,name="blogs_with_type"),
    path('date/<int:year>/<int:month>',views.blogs_with_date,name='blogs_with_date')
]