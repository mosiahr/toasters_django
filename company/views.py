from django.shortcuts import render, redirect

from django.views.generic import ListView, DetailView, UpdateView, View, DeleteView, CreateView
from dj_extensions.views import PaginationMixin

from django.views.generic.edit import FormMixin
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.utils.translation import ugettext as _

from .models import Company, Location, TypeCompany, Price
from gallery.models import Photo
from .forms import CompanyFilterForm, CompanyAddForm, CompanyUpdateForm
from .messages import ErrorMessageMixin

from django.contrib.auth import get_user_model
User = get_user_model()


class CompanyListView(PaginationMixin, ListView):
    form_class = CompanyFilterForm
    context_object_name = 'companies'
    model = Company
    # initial = {'type_company': 'vedushie-tamada'}
    template_name = 'company/company_list.html'
    paginate_by = 10
    paginate_orphans = 2
    n_list = 4    # This mixin provides list of links to previous and next n_list number of pages (PaginationMixin)

    def get_context_data(self, **kwargs):
        context = super(CompanyListView, self).get_context_data(**kwargs)

        if self.request.method == 'GET':
            form = self.form_class(self.request.GET)

            if form.is_valid():
                context.update({'form': form})

            try:
                location = Location.pub_objects.get(slug=self.request.GET['location'])
            except:
                location = None
            try:
                type = TypeCompany.pub_objects.get(slug=self.request.GET['type'])
            except:
                type = None
            try:
                price = Price.pub_objects.get(slug=self.request.GET['price'])
            except:
                price = None

            header = {
                'location': location,
                'type': type,
                'price': price,
            }

        else:
            form = self.form_class()
            header = None

        context.update({'form': form,
                        'header': header})

        return context

    def get_queryset(self):
        try:
            location = self.request.GET['location']
        except:
            location = None
        try:
            type = self.request.GET['type']
        except:
            type = None
        try:
            price = self.request.GET['price']
        except:
            price = None

        if location and type and price:
            return Company.pub_objects.filter(location__slug=location,
                                              type__slug=type,
                                              price__slug=price)

        if location and type:
            return Company.pub_objects.filter(location__slug=location,
                                              type__slug=type)

        if type and price:
            return Company.pub_objects.filter(type__slug=type,
                                              price__slug=price)

        if location and price:
            return Company.pub_objects.filter(location__slug=location,
                                              price__slug=price)

        if location:
            return Company.pub_objects.filter(location__slug=location)

        if type:
            return Company.pub_objects.filter(type__slug=type)

        if price:
            return Company.pub_objects.filter(price__slug=price)

        return Company.pub_objects.all().order_by('-created')


class CompanyDetailView(DetailView):
    model = Company


class CompanyAddView(SuccessMessageMixin,
                     ErrorMessageMixin,
                     LoginRequiredMixin,
                     FormMixin,
                     View):
    form_class = CompanyAddForm
    # form_class = PhotoFormSet
    model = Company
    success_url = '/accounts/'
    success_message = _('Company %(name)s was created successfully!')
    error_message = _('Please correct the errors below.')
    title = _('Add Company')

    def get(self, request):
        if Company.objects.all().filter(user_id=self.request.user.id).exists():
            return redirect(self.success_url)
        # context = {'form': self.get_form(), 'title': self.title}
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
        form.save_m2m()     # save into company_company_type
        return super(CompanyAddView, self).form_valid(form)

    def form_invalid(self, form):
        context = {'form': form, 'title': self.title}
        messages.error(self.request, self.error_message)
        return render(self.request, 'company/company_form.html', context)


# from django.forms import inlineformset_factory
# PhotoFormSet = inlineformset_factory(Company, Photo, exclude=(), extra=1)
#
#
# class CompanyCreate(CreateView):
#     template_name = 'company/company_form_set.html'
#     model = Company
#     # form_class = PhotoFormSet
#     fields = '__all__'
#
#     def get_context_data(self, **kwargs):
#         context = super(CompanyCreate, self).get_context_data(**kwargs)
#         if self.request.POST:
#             context['formset'] = PhotoFormSet(self.request.POST, request.FILES)
#         else:
#             context['formset'] = PhotoFormSet()
#         return context
#
#     def form_valid(self, form):
#         obj = form.save(commit=False)
#         obj.user = User.objects.get(email=self.request.user)
#         obj.save()
#         form.save_m2m()     # save into company_company_type
#         return super(CompanyCreate, self).form_valid(form)
#
#     def form_invalid(self, form):
#         context = {'form': form, 'title': self.title}
#         messages.error(self.request, self.error_message)
#         return render(self.request, 'company/company_form_set.html', context)


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
        self.object = self.get_object()
        context = self.get_context_data(object=self.object, form=self.get_form())
        return render(request, 'company/company_form.html', context)

    def get_object(self, queryset=None):
        obj = Company.objects.get(pk=self.kwargs['pk'])
        return obj

    def get_context_data(self, **kwargs):
        context = super(CompanyUpdateView, self).get_context_data(**kwargs)
        context.update({'title': self.title})
        return context


class CompanyDeleteView(LoginRequiredMixin, DeleteView):
    model = Company
    template_name = 'company/company_confirm_delete.html'
    success_url = '/accounts/'
    success_message = _("Company %(name)s was deleted successfully!")
    title = _("Are you sure?")

    def get_context_data(self, **kwargs):
        context = super(CompanyDeleteView, self).get_context_data(**kwargs)
        context.update({'title': self.title})
        return context

    def get_object(self, queryset=None):
        obj = Company.objects.get(pk=self.kwargs['pk'])
        return obj

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(CompanyDeleteView, self).delete(request, *args, **kwargs)


