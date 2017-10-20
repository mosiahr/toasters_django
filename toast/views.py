from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Toaster, Tag


def hello(request):
    return render(request, 'core/base.html', {'hello': 'hello world !!!'} )


class ToasterListView(ListView):
    model = Toaster

    def get_context_data(self, **kwargs):
        context = super(ToasterListView, self).get_context_data(**kwargs)
        context.update({'toasters': Toaster.objects.all()})
        return context


class ToasterDetailView(DetailView):
    model = Toaster

    # def get_queryset(self):
    #     return Toaster.objects.filter()