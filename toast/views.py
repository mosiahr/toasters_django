from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Toaster, Tag, Location
from .forms import ToasterLocationForm

from django.utils.datastructures import MultiValueDictKeyError

from django.utils.translation import ugettext as _

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from accounts.messages import ErrorMessageMixin


from django.contrib.auth import get_user_model
User = get_user_model()


# class ProfileCreateView(LoginRequiredMixin,
#                         SuccessMessageMixin,
#                         ErrorMessageMixin,
#                         CreateView):
#     form_class = ProfileCreateForm
#     template_name = 'accounts/detail_update_view.html'
#     success_message = _("Your account %(email)s was updated successfully!")
#     error_message = _('Please correct the errors below.')
#
#     def get_object(self, queryset=None):
#         return self.request.user
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(ProfileCreateView, self).get_context_data(*args, **kwargs)
#         context['title'] = _('Change Your Account Details')
#         return context
#
#     def get_success_url(self):
#         return reverse("accounts:home")
#
#     def form_valid(self, form):
#         """
#         If the form is valid, save the associated model.
#         """
#         # user = User.objects.get(pk=id)
#         self.object = form.save()
#         return super(ProfileCreateView, self).form_valid(form)


# class ProfileView(SuccessMessageMixin, ErrorMessageMixin, CreateView):
#     form_class = RegisterForm
#     template_name = 'accounts/register.html'
#     success_url = '/accounts/login/'
#     success_message = _("%(email)s was created successfully")
#     error_message = _('Please correct the errors below.')

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



