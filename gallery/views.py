from django.shortcuts import render

from django.views.generic import ListView, DetailView, UpdateView, View, DeleteView
from django.utils.translation import ugettext as _


from .models import Album, Photo


class AlbumListView(ListView):
    model = Album
    template_name = 'gallery/album_list.html'
    context_object_name = 'albums'
    title = _('Albums')

    def get_context_data(self, **kwargs):
        context = super(AlbumListView, self).get_context_data(**kwargs)
        context.update({'title': self.title})
        return context


class PhotoListView(ListView):
    model = Photo
    template_name = 'gallery/gallery_list.html'
    context_object_name = 'photos'


    # def get_context_data(self, **kwargs):
    #     context = super(PhotoListView, self).get_context_data(**kwargs)
    #     # context.update({'title': self.title})
    #     return context

    def get_queryset(self):
        return Photo.objects.filter(album__slug=self.kwargs['album']).order_by('-created')
