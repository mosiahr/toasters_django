from django.conf.urls import url

from .views import (
    AlbumListView,
    PhotoListView,
    PhotoAddView,
    AlbumAddView,
    AlbumUpdateView,
    AlbumDeleteView,

    PhotosListView,
)


urlpatterns = [
    url(r'^albums/$', AlbumListView.as_view(), name='albums'),
    url(r'^album/(?P<pk>\d+)/$', PhotoListView.as_view(), name='photo'),
    url(r'^photo-add/$', PhotoAddView.as_view(), name='photo_add'),
    url(r'^album/add/$', AlbumAddView.as_view(), name='album_add'),
    url(r'^album/(?P<pk>\d+)/update/$', AlbumUpdateView.as_view(), name='album_update'),
    url(r'^album/(?P<pk>\d+)/delete/$', AlbumDeleteView.as_view(), name='album_delete'),

    url(r'^photos/$', PhotosListView.as_view(), name='photos'),

    # url(r'^add/$', CompanyAddView.as_view(), name='company_add'),
    # url(r'^update/(?P<pk>\d+)/$', CompanyUpdateView.as_view(), name='company_update'),
    # url(r'^delete/(?P<pk>\d+)/$', CompanyDeleteView.as_view(), name='company_delete'),
    # url(r'^(?P<pk>\d+)/$', CompanyDetailView.as_view(), name='company_detail'),
    # url(r'^profile_update/$', ProfileCreateView.as_view(), name='profile-update'),
]
