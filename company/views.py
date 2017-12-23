from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Company


class CompanyListView(ListView):
    model = Company
    context_object_name = 'companies'
    # form_class = ToasterLocationForm

    # def get_context_data(self, **kwargs):
    #     context = super(ToasterListView, self).get_context_data(**kwargs)
    #     header = None
    #     if self.request.method == 'GET':
    #         form = self.form_class(self.request.GET)
    #         if form.is_valid():
    #             context.update({'form': form})
    #         try:
    #             header = Location.objects.get(slug=self.request.GET['location_select']).name
    #         except:
    #             pass
    #     else:
    #         form = self.form_class()
    #     context.update({'form': form, 'header': header})
    #     return context

    # def get_queryset(self):
    #     try:
    #         if self.request.GET['location_select']:
    #             location = self.request.GET['location_select']
    #             return Toaster.pub_objects.filter(locations__slug=location)
    #     except MultiValueDictKeyError:
    #         pass
    #     return Toaster.pub_objects.all().order_by('-created')


class CompanyDetailView(DetailView):
    model = Company
