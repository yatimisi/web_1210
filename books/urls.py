from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='books-index'),
    path('<int:pk>/', views.show, name='book-show'),
    path('add/', views.add, name='books-add'),
    path('<int:pk>/edit/', views.edit, name='books-edit'),
    path('<int:pk>/delete/', views.delete, name='books-delete'),
]