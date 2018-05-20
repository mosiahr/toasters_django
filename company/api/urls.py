from django.conf.urls import url

from .views import CompanyListAPIView, SessionAPIView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', SessionAPIView.as_view(), name='favorite'),
    url(r'^list/$', CompanyListAPIView.as_view(), name='company_list'),
]