from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic.edit import FormMixin

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.utils.translation import ugettext as _

from .models import Company, Location, TypeCompany, Price
from .forms import CompanyLocationForm, CompanyAddForm, CompanyUpdateForm
from .messages import ErrorMessageMixin

from django.contrib.auth import get_user_model
User = get_user_model()


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


class CompanyAddView(SuccessMessageMixin,
                    ErrorMessageMixin,
                    LoginRequiredMixin,
                    FormMixin,
                    View):
    form_class = CompanyAddForm
    model = Company
    success_url = '/accounts/'
    success_message = _("Company %(name)s was created successfully!")
    error_message = _('Please correct the errors below.')
    title = _('Add Company')

    def get(self, request):
        if Company.objects.all().filter(user_id=self.request.user.id).exists():
            # messages.error(self.request, "Your company already exists!")
            return redirect(self.success_url)
        context = {'form': self.get_form(), 'title': self.title}
        return render(request, 'company/company_form.html', context)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = User.objects.get(email=self.request.user)
        obj.save()
        return super(CompanyAddView, self).form_valid(form)


    def form_invalid(self, form):
        context = {'form': form, 'title': self.title}
        messages.error(self.request, self.error_message)
        return render(self.request, 'company/company_form.html', context)

from django.core.exceptions import ObjectDoesNotExist


class CompanyUpdateView(LoginRequiredMixin,
                       SuccessMessageMixin,
                       ErrorMessageMixin,
                       UpdateView):
    

    form_class = CompanyUpdateForm
    model = Company
    success_url = '/accounts/'
    success_message = _("Сompany %(name)s was updated successfully!")
    error_message = _('Please correct the errors below.')
    title = _('Сhange of company')


    def get(self, request, **kwargs):
        try:
            self.object = Company.objects.get(pk=self.kwargs['pk'])
        except Company.DoesNotExist:
            return redirect(self.success_url)
        
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form, title = self.title)
        return render(request, 'company/company_form.html', context)

    def get_object(self, queryset=None):
        obj = Company.objects.get(pk=self.kwargs['pk'])
        return obj

