from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.utils.datastructures import MultiValueDictKeyError
from django.db.models import Q

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
            location = self.request.GET['location_select']
            type_company = self.request.GET['type_company']
            price = self.request.GET['price']
            if self.request.GET['location_select'] and self.request.GET['type_company'] and self.request.GET['price']:
                return Company.pub_objects.filter(locations__slug=location,
                                                  type__slug=type_company,
                                                  price__slug=price)

            if self.request.GET['location_select'] and self.request.GET['type_company']:
                return Company.pub_objects.filter(locations__slug=location,
                                                  type__slug=type_company)

            if self.request.GET['type_company'] and self.request.GET['price']:
                return Company.pub_objects.filter(type__slug=type_company,
                                                  price__slug=price)

            if self.request.GET['location_select'] and self.request.GET['price']:
                return Company.pub_objects.filter(locations__slug=location,
                                                  price__slug=price)

            if self.request.GET['location_select']:
                return Company.pub_objects.filter(locations__slug=location)

            if self.request.GET['type_company']:
                return Company.pub_objects.filter(type__slug=type_company)

            if self.request.GET['price']:
                return Company.pub_objects.filter(price__slug=price)

        except MultiValueDictKeyError:
            pass
        return Company.pub_objects.all().order_by('-created')


class CompanyDetailView(DetailView):
    model = Company
