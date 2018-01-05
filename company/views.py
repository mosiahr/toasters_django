from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.utils.datastructures import MultiValueDictKeyError
from django.db.models import Q

from .models import Company, Location, TypeCompany, Price
from .forms import CompanyLocationForm


class CompanyListView(ListView):
    model = Company
    context_object_name = 'companies'
    form_class = CompanyLocationForm
    # initial = {'type_company': 'vedushie-tamada'}
    template_name = 'company/company_list.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyListView, self).get_context_data(**kwargs)
        header = None

        if self.request.method == 'GET':
            form = self.form_class(self.request.GET)

            if form.is_valid():
                context.update({'form': form})

            try:
                location_select_name = Location.objects.get(slug=self.request.GET['location_select']).name
            except:
                location_select_name = None

            try:
                type_company_name = TypeCompany.objects.get(slug=self.request.GET['type_company']).name
            except:
                type_company_name = None

            try:
                price_name = Price.objects.get(slug=self.request.GET['price']).name
            except:
                price_name = None

            header = {
                'location': location_select_name,
                'type': type_company_name,
                'price': price_name,
            }

        else:
            form = self.form_class()

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
