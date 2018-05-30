from django.contrib.sessions.models import Session
from rest_framework import generics
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.response import Response
from .serializers import SessionSerializer, CompanySerializer
from company.models import Company


class CompanyListAPIView(ListAPIView):
    serializer_class = CompanySerializer

    def get_favorites(self):
        if self.request.session.__contains__('favorite'):
            return self.request.session.get('favorite')
        return dict()

    def get_queryset(self):
        # qs = []
        # for comp in Company.pub_objects.all():
        #     if comp.id in self.get_favorites():
        #         qs.append(comp)
        return [comp for comp in Company.pub_objects.all()
                if int(comp.id) in self.get_favorites()]

    # def get_context_data(self, **kwargs):
    #     super(CompanyListAPIView, self).get_context_data(**kwargs)


class SessionAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SessionSerializer

    def get(self, request, *args, **kwargs):

        # Create session
        if not request.session.exists(request.session.session_key):
            request.session.create()
            print('Create session, ', request.session.session_key)

        # Create favorite
        if not request.session.__contains__('favorite'):
            request.session.__setitem__('favorite', [])

        try:
            # Add pk to favorite
            if int(self.kwargs['pk']) not in request.session['favorite']:
                self.serializer_class.create(self, request)
                
            # Delete pk to favorite
            else:
                self.serializer_class.update(self, request)
        except Exception as e:
            print(e)

        print("Session['favorite']: ", request.session['favorite'])

        # key = request.session.session_key
        #
        # s = Session.objects.get(pk=key)
        # # print(s.expire_date)
        # # print(s.session_data)
        # p = s.get_decoded()
        # # print(p)

        count_fav = None
        # Count favorite
        if request.session.__contains__('favorite'):
            count_fav = len(self.request.session['favorite'])

        # queryset = self.get_queryset()
        # serializer = SessionSerializer(queryset, many=True)
        # return Response(serializer.data)
        data = dict(count_fav=count_fav)
        return Response(data)
