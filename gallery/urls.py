from django.conf.urls import url

from .views import AlbumListView, PhotoListView

urlpatterns = [
    url(r'^albums/$', AlbumListView.as_view(), name='albums'),
    url(r'^album/(?P<album>[\w-]+)/$', PhotoListView.as_view(), name='photo'),
    # url(r'^add/$', CompanyAddView.as_view(), name='company_add'),
    # url(r'^update/(?P<pk>\d+)/$', CompanyUpdateView.as_view(), name='company_update'),
    # url(r'^delete/(?P<pk>\d+)/$', CompanyDeleteView.as_view(), name='company_delete'),
    # url(r'^(?P<pk>\d+)/$', CompanyDetailView.as_view(), name='company_detail'),
    # url(r'^profile_update/$', ProfileCreateView.as_view(), name='profile-update'),

]