from django.conf.urls import url

from .views import (
    TagListView,
    TagDetailView,
)

urlpatterns = [
    url(r'list/$', TagListView.as_view(), name='tag_list'),
    url(r'^(?P<slug>[-\w]+)/$', TagDetailView.as_view(), name='tag_detail'),
]