from django.shortcuts import render, render_to_response
from django.db import transaction

from django.views.generic import ListView, DetailView, UpdateView, View, DeleteView, CreateView
from django.utils.translation import ugettext as _

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .messages import ErrorMessageMixin
from .models import Album, Photo

from .forms import PhotoAddForm, AlbumForm, PhotoFormSet


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


class PhotoAddView(SuccessMessageMixin,
                   ErrorMessageMixin,
                   LoginRequiredMixin,
                   CreateView):
    form_class = PhotoAddForm
    model = Photo
    # fields = '__all__'
    success_url = '/accounts/'
    success_message = _('Photo %(name)s was created successfully!')
    error_message = _('Please correct the errors below.')
    title = _("Add Photo")

    def get_context_data(self, **kwargs):
        context = super(PhotoAddView, self).get_context_data(**kwargs)
        context.update({'title': self.title})
        return context


class AlbumCreateView(SuccessMessageMixin,
                      ErrorMessageMixin,
                      LoginRequiredMixin,
                      CreateView):
    error_message = _('Please correct the errors below.')
    # form_class = PhotoFormSet
    fields = ['name', 'slug', 'summary']
    model = Album
    success_url = '/accounts/'
    success_message = _('Photo %(name)s was created successfully!')
    template_name = 'gallery/manage_photo.html'
    title = _("Add Album")

    # def get(self, request, *args, **kwargs):
    #     self.object = None
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     photo_form = PhotoFormSet()
    #     photo_form_helper = PhotoFormSet()
    #
    #     return self.render_to_response(
    #         self.get_context_data(form=form, photo_form=photo_form)
    #     )
    #
    # def post(self, request, *args, **kwargs):
    #     self.object = None
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     photo_form = PhotoFormSet(self.request.POST)
    #
    #     if (form.is_valid() and photo_form.is_valid()):
    #         return self.form_valid(form, photo_form)
    #     return self.form_invalid(form, photo_form)

    def form_valid(self, form):
        context = self.get_context_data()
        photo_form = context['photo_form']
        with transaction.atomic():
            self.object = form.save()
            # print(photo_form.__dir__())
            # print([(form.errors, form.__dir__(), form.data) for form in photo_form.forms])
            if photo_form.is_valid():
                try:
                    photo_form.instance = self.object
                    photo_form.save()
                except Exception as e:
                    print(e)
            else:
                print('not_valid')

        return super(AlbumCreateView, self).form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data()
        photo_form = context['photo_form']
        messages.error(self.request, self.error_message)
        return self.render_to_response(
            self.get_context_data(form=form, photo_form=photo_form)
        )

    def get_context_data(self, **kwargs):
        ctx = super(AlbumCreateView, self).get_context_data(**kwargs)
        ctx.update({'title': self.title})
        # photo_form_helper = PhotoFormHelper()
        if self.request.POST:
            # form_class = self.get_form_class()
            # ctx['form'] = self.get_form(form_class)(self.request.POST)
            # ctx['form'] = AlbumForm(self.request.POST)
            ctx['photo_form'] = PhotoFormSet(self.request.POST, self.request.FILES)
            # ctx['photo_form_helper'] = PhotoFormHelper()
        else:
            # form_class = self.get_form_class()
            # ctx['form'] = self.get_form(form_class)
            # ctx['form'] = AlbumForm()
            ctx['photo_form'] = PhotoFormSet()
            # ctx['photo_form_helper'] = PhotoFormHelper()
        return ctx
