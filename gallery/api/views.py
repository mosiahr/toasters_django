from rest_framework import generics
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.response import Response
from .serializers import PhotoSerializer
from gallery.models import Photo


class PhotoListAPIView(ListAPIView):
    queryset = Photo.pub_objects.all()
    serializer_class = PhotoSerializer

    # def get_favorites(self):
    #     if self.request.session.__contains__('favorite'):
    #         return self.request.session.get('favorite')
    #     return dict()

    # def get_queryset(self):
    #     # qs = []
    #     # for comp in Company.pub_objects.all():
    #     #     if comp.id in self.get_favorites():
    #     #         qs.append(comp)
    #     return [comp for comp in Photo.pub_objects.all()
    #             if int(comp.id) in self.get_favorites()]

    # def get_context_data(self, **kwargs):
    #     super(CompanyListAPIView, self).get_context_data(**kwargs)