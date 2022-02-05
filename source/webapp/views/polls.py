from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.views.base import TemplateView, FormView as CustomFormView
from webapp.forms import PollForm, PollDeleteForm
from webapp.models import Poll

class IndexView(ListView):
    model = Poll
    context_object_name = "polls"
    template_name = "polls/index.html"
    paginate_by = 5
    paginate_orphans = 0

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by("-created_at").reverse().order_by("question").reverse()


class CreatePollView(CreateView):
    model = Poll
    form_class = PollForm
    template_name = "polls/create.html"


class PollView(DetailView):
    model = Poll
    template_name = "polls/view.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PollUpdateView(UpdateView):
    form_class = PollForm
    template_name = "polls/update.html"
    model = Poll


class PollDeleteView(DeleteView):
    model = Poll
    template_name = "polls/delete.html"
    success_url = reverse_lazy('main_page')

    def dispatch(self, request, *args, **kwargs):
        if self.request.method == "POST":
            self.object_form = PollDeleteForm(instance=self.get_object(), data=self.request.POST)
        else:
            self.object_form = PollDeleteForm()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.object_form
        return context

    def post(self, request, *args, **kwargs):
        if self.object_form.is_valid():
            return super().delete(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)