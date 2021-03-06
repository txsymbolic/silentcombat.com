from django.urls import path

from . import views

urlpatterns = [
    path('', views.entries, name='news'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('news/', views.posts, name='news'),
    path('<int:id>/', views.read),
]