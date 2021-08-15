from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('view/', views.display, name="display"),
    path('',views.create, name="create"),
    path('<int:id>/',views.create, name="edit"),
    path('delete/<int:id>/',views.delete, name="delete"),
]
