from django.conf.urls import url

from .views import CompanyListView, CompanyDetailView

urlpatterns = [
    url(r'^$', CompanyListView.as_view(), name='companies'),
    url(r'^(?P<pk>\d+)/$', CompanyDetailView.as_view(), name='company_detail'),
    # url(r'tags/$', TagListView.as_view(), name='tags'),
    # url(r'^tags/(?P<slug>[-\w]+)/$', TagDetailView.as_view(), name='tag_detail'),
    # url(r'^profile_update/$', ProfileCreateView.as_view(), name='profile-update'),
]