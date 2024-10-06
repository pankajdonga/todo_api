from django.contrib import admin
from django.urls import path
from todoapp import views

urlpatterns = [
    path('',views.task_list),
    path('task_create/',views.task_create),
    path('task_detail/<int:id>',views.task_detail),
    path('task_update/<int:id>',views.task_update),
    path('task_delete/<int:id>',views.task_delete),
    path('task_select_update/<int:id>',views.task_select_update),
]