from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .views import (
    AccountHomeView,
    AccountActivateView,
    LoginView,
    RegisterView,
    DoneRegisterView,
    UserDetailUpdateView,
    UserPasswordChangeView,
)

urlpatterns = [
    url(r'^$', AccountHomeView.as_view(), name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^register/done/$', DoneRegisterView.as_view(), name='register_done'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        AccountActivateView.as_view(), name='activate'),
    url(r'^password/$', UserPasswordChangeView.as_view(), name='change_password'),
    url(r'^details/$', UserDetailUpdateView.as_view(), name='user-update'),

    # Password Reset View
    url(r'^password_reset/$',
        auth_views.password_reset, {
            'template_name': 'password_reset/password_reset_form.html',
            'email_template_name': 'password_reset/password_reset_email.html',
            'subject_template_name': 'password_reset/password_reset_subject.txt',
            'post_reset_redirect': 'accounts:password_reset_done',
        },
        name='password_reset'),

    url(r'^password_reset/done/$', auth_views.password_reset_done, {
        'template_name': 'password_reset/password_reset_done.html',
        },
        name='password_reset_done'),

    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, {
            'template_name': 'password_reset/password_reset_confirm.html',
            'post_reset_redirect': 'accounts:password_reset_complete',
        },
        name='password_reset_confirm'),

    url(r'^reset/done/$', auth_views.password_reset_complete, {
        'template_name': 'password_reset/password_reset_complete.html',
        },
        name='password_reset_complete')
]

