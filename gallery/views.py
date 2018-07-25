from django.shortcuts import render, render_to_response
from django.db import transaction
from django.http import HttpResponseRedirect

from django.views.generic import ListView, DetailView, UpdateView, View, DeleteView, CreateView
from django.utils.translation import ugettext as _

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .messages import ErrorMessageMixin
from .models import Album, Photo

from .forms import PhotoAddForm, AlbumForm, PhotoFormSet

from company.models import Company


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
    template_name = 'gallery/photo_list.html'
    context_object_name = 'photos'

    def get_context_data(self, **kwargs):
        context = super(PhotoListView, self).get_context_data(**kwargs)
        current_album = Album.objects.get(id=self.kwargs['pk'])
        current_company = current_album.company
        more_albums = [album for album in Album.objects.filter(company_id=current_company.id)
                       if album.is_album_empty() is False]
        context.update({
            'current_album': current_album,
            'current_company': current_company,
            'more_albums': more_albums,
        })
        return context

    def get_queryset(self):
        return Photo.objects.filter(album_id=self.kwargs['pk']).order_by('-created')


class PhotoAddView(SuccessMessageMixin,
                   ErrorMessageMixin,
                   LoginRequiredMixin,
                   CreateView):
    form_class = PhotoAddForm
    model = Photo
    success_url = reverse_lazy('accounts:dashboard')
    success_message = _('Photo %(name)s was created successfully!')
    error_message = _('Please correct the errors below.')
    title = _("Add Photo")

    def get_context_data(self, **kwargs):
        context = super(PhotoAddView, self).get_context_data(**kwargs)
        context.update({'title': self.title})
        return context

    def get_form_kwargs(self):
        kwargs = super(PhotoAddView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_invalid(self, form):
        context = {'form': form, 'title': self.title}
        messages.error(self.request, self.error_message)
        return render(self.request, 'gallery/photo_form.html', context)


class AlbumAddView(SuccessMessageMixin,
                   ErrorMessageMixin,
                   LoginRequiredMixin,
                   CreateView):
    error_message = _('Please correct the errors below.')
    form_class = AlbumForm
    model = Album
    success_url = reverse_lazy('accounts:dashboard')
    success_message = _('Album "%(name)s" was created successfully!')
    template_name = 'gallery/manage_photo.html'
    title = _("Сreate an album")

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        photo_form = PhotoFormSet()
        return self.render_to_response(
            self.get_context_data(form=form, photo_form=photo_form)
        )

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        photo_form = PhotoFormSet(self.request.POST, self.request.FILES, instance=self.object)

        if form.is_valid() and photo_form.is_valid():
            return self.form_valid(form, photo_form)
        else:
            return self.form_invalid(form, photo_form)

    def get_form_kwargs(self):
        kwargs = super(AlbumAddView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form, photo_form):
        with transaction.atomic():
            self.object = form.save()
            if photo_form.is_valid():
                photo_form.instance = self.object
                photo_form.save()
        return super(AlbumAddView, self).form_valid(form)

    def form_invalid(self, form, photo_form):
        messages.error(self.request, self.error_message)
        return self.render_to_response(
            self.get_context_data(form=form, photo_form=photo_form)
        )

    def get_context_data(self, **kwargs):
        ctx = super(AlbumAddView, self).get_context_data(**kwargs)
        ctx.update({'title': self.title})
        if self.request.POST:
            form_class = self.get_form_class()
            ctx['form'] = form_class(self.request.POST, instance=self.object)
            ctx['photo_form'] = PhotoFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            form_class = self.get_form_class()
            ctx['form'] = self.get_form(form_class)
            ctx['photo_form'] = PhotoFormSet(instance=self.object)
        return ctx


class AlbumUpdateView(SuccessMessageMixin,
                      ErrorMessageMixin,
                      LoginRequiredMixin,
                      UpdateView):
    error_message = _('Please correct the errors below.')
    form_class = AlbumForm
    model = Album
    success_url = reverse_lazy('accounts:dashboard')
    success_message = _('Album "%(name)s" was updated successfully!')
    template_name = 'gallery/manage_photo.html'
    title = _("Update Album")

    def get_object(self, queryset=None):
        obj = Album.objects.get(pk=self.kwargs['pk'])
        return obj

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        photo_form = PhotoFormSet(self.request.FILES, instance=self.object)
        return self.render_to_response(
            self.get_context_data(form=form, photo_form=photo_form)
        )

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        photo_form = PhotoFormSet(self.request.POST, self.request.FILES, instance=self.object)

        if form.is_valid() and photo_form.is_valid():
            return self.form_valid(form, photo_form)
        else:
            return self.form_invalid(form, photo_form)

    def get_form_kwargs(self):
        kwargs = super(AlbumUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form, photo_form):
        with transaction.atomic():
            self.object = form.save()
            if photo_form.is_valid():
                photo_form.instance = self.object
                photo_form.save()
        return super(AlbumUpdateView, self).form_valid(form)

    def form_invalid(self, form, photo_form):
        messages.error(self.request, self.error_message)
        return self.render_to_response(
            self.get_context_data(form=form, photo_form=photo_form)
        )

    def get_context_data(self, **kwargs):
        ctx = super(AlbumUpdateView, self).get_context_data(**kwargs)
        ctx.update({'title': self.title})
        if self.request.POST:
            form_class = self.get_form_class()
            ctx['form'] = form_class(self.request.POST, instance=self.object)
            ctx['photo_form'] = PhotoFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            form_class = self.get_form_class()
            ctx['form'] = self.get_form(form_class)
            ctx['photo_form'] = PhotoFormSet(instance=self.object)
        return ctx


class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = Album
    template_name = 'gallery/album_confirm_delete.html'
    success_url = reverse_lazy('accounts:dashboard')
    success_message = _('Album "%(name)s" was deleted successfully!')
    title = _("Are you sure?")

    def get_context_data(self, **kwargs):
        context = super(AlbumDeleteView, self).get_context_data(**kwargs)
        context.update({'title': self.title})
        return context

    def get_object(self, queryset=None):
        obj = Album.objects.get(pk=self.kwargs['pk'])
        return obj

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(AlbumDeleteView, self).delete(request, *args, **kwargs)