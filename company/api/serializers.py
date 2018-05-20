from rest_framework import serializers
from django.contrib.sessions.models import Session

# from django.contrib.auth.models import User
# from django.contrib.auth.validators import UnicodeUsernameValidator

from company.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class SessionSerializer(serializers.Serializer):
    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super(SessionSerializer, self).__init__(*args, **kwargs)

    def create(self, request):
        request.session['favorite'].append(int(self.kwargs['pk']))
        request.session.modified = True

    def update(self, request):
        request.session['favorite'].remove(int(self.kwargs['pk']))
        request.session.modified = True
