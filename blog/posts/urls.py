from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('<int:id>/', views.post, name="post"),
    path('join/', views.join, name='join')
]
