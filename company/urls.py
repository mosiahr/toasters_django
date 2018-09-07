from django.conf.urls import url

from .views import (
    CompanyListView,
    CompanyAddView,
    CompanyDetailView,
    CompanyUpdateView,
    CompanyDeleteView,
    # CompanyCreate
)

urlpatterns = [
    # url(r'^$', CompanyListView.as_view(), name='companies'),
    url(r'^filter/(?P<location>[a-z\-]+)?/?(?P<type>[a-z\-]+)?/?(?P<price>[a-z0-9\-]+)?/?$', CompanyListView.as_view(), name='companies'),
    # url(r'^toaster/$', CompanyListView.as_view(), name='companies'),
    url(r'^add/$', CompanyAddView.as_view(), name='company_add'),
    # url(r'^add/$', CompanyCreate.as_view(), name='company_add'),
    url(r'^update/(?P<pk>\d+)/$', CompanyUpdateView.as_view(), name='company_update'),
    url(r'^delete/(?P<pk>\d+)/$', CompanyDeleteView.as_view(), name='company_delete'),
    url(r'^(?P<pk>\d+)/$', CompanyDetailView.as_view(), name='company_detail'),
    # url(r'^profile_update/$', ProfileCreateView.as_view(), name='profile-update'),
]


