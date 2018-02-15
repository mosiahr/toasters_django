from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Tag
from company.models import Company


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
        context.update({'companies': Company.objects.filter(tags=Tag.objects.get(slug=self.object.slug))})
        return context
