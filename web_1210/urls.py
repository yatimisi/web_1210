"""web_1210 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# from . import views
# from books import views as book_views

# def root(request):
#     return redirect('books-index')

urlpatterns = [
    # django admin jet
    # https://github.com/geex-arts/django-jet

    # path('', views.root),
    # path('<str:name>/', views.hello),
    # path('s/<int:number>/', views.s),
    # path('l/<int:number1>/<int:number2>/', views.l),
    path('', lambda request: redirect('books-index'), name='root'), # lambda=不具名變數
    path('books/', include('books.urls')),

    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
]
