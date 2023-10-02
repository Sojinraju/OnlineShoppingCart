from  . import views
from django.contrib import admin
from django.urls import path, include
app_name='shop_app'
urlpatterns = [

    path('',views.allProCat,name='allProCat'),
    path('<slug:c_slug>/',views.allProCat,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='proDetail'),
]