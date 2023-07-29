from django.contrib import admin
from django.urls import path
from testApp import views


urlpatterns = [
    path('',views.home),
    path('add/',views.add),
    path('update/<int:id>/', views.update),
    path('delete/<int:id>/', views.delete),
]
