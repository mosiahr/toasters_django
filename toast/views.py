from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Toaster, Tag

from django.utils.datastructures import MultiValueDictKeyError



def hello(request):
    return render(request, 'core/base.html', {'hello': 'hello world !!!'} )


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

    # def get_context_data(self, **kwargs):
    #     context = super(ToasterListView, self).get_context_data(**kwargs)
    #     context.update({'toasters': Toaster.objects.all()})
    #     return context

    context_object_name = 'toasters'

    def get_queryset(self):
        try:
            if self.request.GET['location']:
                location = self.request.GET['location']
                return Toaster.pub_objects.filter(locations__slug=location)
        except MultiValueDictKeyError:
            pass
        return Toaster.pub_objects.all()


class ToasterDetailView(DetailView):
    model = Toaster

    # def get_queryset(self):
    #     return Toaster.objects.filter()



