# coding: utf-8

"""example01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

from example01.views import HomeView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    
    url(r'^photo/', include('photo.urls', namespace='photo')),

    # Class-based views for Bookmark app
    #url(r'^bookmark/$', BookmarkLV.as_view(), name='index'),
    #url(r'^bookmark/(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),
    
    # View가 간단할 경우 urls.py에서 처리 가능, 예시
    # url(r'^bookmark/$', ListView.as_view(model=Bookmark), name='index'),
    # url(r'^bookmark/?P<pk>\d+/$', DetailView.as_view(model=Bookmark), name='detail'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
