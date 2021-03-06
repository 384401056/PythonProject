"""django_Q URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^', include('app01.urls')), # 间接指定URL到app01下的urls文件中
    # url(r'^', include('FormValidation.urls')), # 间接指定URL到FormValidation下的urls文件中
    # url(r'^', include('CookiesAndSession.urls')) # 间接指定URL到CookiesOpt下的urls文件中
    # url(r'^', include('CookiesOpt.urls')) # 间接指定URL到CookiesOpt下的urls文件中
    # url(r'^', include('Session.urls')) # 间接指定URL到CookiesOpt下的urls文件中
    # url(r'^', include('Middleware.urls')) # 间接指定URL到CookiesOpt下的urls文件中
    # url(r'^', include('Cache.urls')) # 间接指定URL到CookiesOpt下的urls文件中
    url(r'^', include('Signals.urls')) # 间接指定URL到CookiesOpt下的urls文件中
    # url(r'^', include('FileUpload.urls')) # 间接指定URL到CookiesOpt下的urls文件中

]
