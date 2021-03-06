"""toasters URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

import django.views.static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # url(r'^toasters/', include('toast.urls', namespace='toast')),
    url(r'^company/', include('company.urls', namespace='company')),
    url(r'^tags/', include('tags.urls', namespace='tags')),
    url(r'gallery/', include('gallery.urls', namespace='gallery')),

    url(r'^media/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT}),

    url(r'^accounts/', include('accounts.urls', namespace='accounts')),

    url(r'^api/v1/company/', include('company.api.urls', namespace='api_company')),
    url(r'^api/v1/gallery/', include('gallery.api.urls', namespace='api_gallery'))
]

# if settings.DEBUG:
#     if settings.MEDIA_URL:
#         urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
#         urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

