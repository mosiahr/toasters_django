from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Toaster, Tag


def hello(request):
    return render(request, 'core/base.html', {'hello': 'hello world !!!'} )


class ToasterListView(ListView):
    model = Toaster

    # def get_context_data(self, **kwargs):
    #     context = super(ToasterListView, self).get_context_data(**kwargs)
    #     context.update({'toasters': Toaster.objects.all()})
    #     return context

    context_object_name = 'toasters'

    def get_queryset(self):
        return Toaster.objects.all()


class ToasterDetailView(DetailView):
    model = Toaster

    # def get_queryset(self):
    #     return Toaster.objects.filter()

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

