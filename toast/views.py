from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import Toaster, Tag, Location
from .forms import ToasterLocationForm

from django.utils.datastructures import MultiValueDictKeyError


class TagListView(ListView):
    model = Tag

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        context.update({'tags': Tag.objects.all()})
        return context


class TagDetailView(DetailView):
    model = Tag

    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(TagDetailView, self).get_context_data(**kwargs)
        context.update({'toasters': Toaster.objects.filter(tags=Tag.objects.get(slug=self.object.slug))})
        return context


class ToasterListView(ListView):
    model = Toaster
    context_object_name = 'toasters'
    form_class = ToasterLocationForm

    def get_context_data(self, **kwargs):
        context = super(ToasterListView, self).get_context_data(**kwargs)
        header = None
        if self.request.method == 'GET':
            form = self.form_class(self.request.GET)
            if form.is_valid():
                context.update({'form': form})
            try:
                header = Location.objects.get(slug=self.request.GET['location_select']).name
            except:
                pass
        else:
            form = self.form_class()
        context.update({'form': form, 'header': header})
        return context

    def get_queryset(self):
        try:
            if self.request.GET['location_select']:
                location = self.request.GET['location_select']
                return Toaster.pub_objects.filter(locations__slug=location)
        except MultiValueDictKeyError:
            pass
        return Toaster.pub_objects.all().order_by('-created')


class ToasterDetailView(DetailView):
    model = Toaster

    # def get_queryset(self):
    #     return Toaster.objects.filter()



