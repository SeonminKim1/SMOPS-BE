"""smops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from art.views import TestProductView
from django.contrib import admin
from django.urls import path
from user.views import TestUserView

urlpatterns = [
    path("admin/", admin.site.urls),
    ## Test 용 URL 입니다.
    path("get_users/", TestUserView.as_view()),
    path("get_products/", TestProductView.as_view()),
]
