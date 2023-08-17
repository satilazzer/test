from django.urls import path

from . import views


app_name = 'main'
urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('sign_up/', views.sign_up, name = 'sign_up'),
    path('send_msg/', views.send_msg, name = "send_msg")
]
