from django.urls import path
from. import views

urlpatterns = [
     path('', views.index, name='index'),
     path('form', views.form, name='form'),
     path('update-user/<str:pk>/', views.update_user, name='update-user'),
     path('read-user/<str:pk>/', views.read_user, name='read-user'),
]