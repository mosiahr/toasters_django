from django.conf.urls import url

from .views import PhotoListAPIView

urlpatterns = [
    # url(r'^(?P<pk>\d+)/$', SessionAPIView.as_view(), name='favorite'),
    url(r'^photo-list/$', PhotoListAPIView.as_view(), name='photo_list'),
]