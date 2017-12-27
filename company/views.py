from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.utils.datastructures import MultiValueDictKeyError

from .models import Company, Location
from .forms import CompanyLocationForm


class CompanyListView(ListView):
    model = Company
    context_object_name = 'companies'
    form_class = CompanyLocationForm

    def get_context_data(self, **kwargs):
        context = super(CompanyListView, self).get_context_data(**kwargs)
        header = None
        if self.request.method == 'GET':
            form = self.form_class(self.request.GET)
            # form = self.form_class(self.request.GET, initial={'location_select': 'kiev'})
            # form.fields['location_select'].initial = 'kiev'

            if form.is_valid():
                context.update({'form': form})
            try:
                header = Location.objects.get(slug=self.request.GET['location_select']).name
            except:
                pass

        else:
            # form = self.form_class(initial={'location_select': 'kiev'})
            form = self.form_class()
            # form.fields['location_select'].initial = 'kiev'
        context.update({'form': form, 'header': header})
        return context

    def get_queryset(self):
        try:
            if self.request.GET['location_select'] and self.request.GET['type_company']:
                location = self.request.GET['location_select']
                type = self.request.GET['type_company']
                return Company.pub_objects.filter(locations__slug=location, type__slug=type)
            if self.request.GET['location_select']:
                location = self.request.GET['location_select']
                return Company.pub_objects.filter(locations__slug=location)
            if self.request.GET['type_company']:
                type = self.request.GET['type_company']
                return Company.pub_objects.filter(type__slug=type)
        except MultiValueDictKeyError:
            pass
        return Company.pub_objects.all().order_by('-created')


class CompanyDetailView(DetailView):
    model = Company
