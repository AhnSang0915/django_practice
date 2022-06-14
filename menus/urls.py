from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('food/<int:pk>/', views.detail),  # 수정해주세요.
]
