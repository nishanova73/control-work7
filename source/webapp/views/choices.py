from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, ListView, CreateView, UpdateView, DeleteView

from webapp.views.base import TemplateView, FormView as CustomFormView
from webapp.forms import ChoiceForm, ChoiceDeleteForm
from webapp.models import Choice, Poll

class CreateChoiceView(CreateView):
    model = Choice
    template_name = 'choices/create.html'
    form_class = ChoiceForm

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choice = form.save(commit=False)
        choice.poll = poll
        choice.save()
        return redirect('poll_view', pk=poll.pk)

class ChoiceUpdateView(UpdateView):
    form_class = ChoiceForm
    template_name = "choices/update.html"
    model = Choice

    def get_success_url(self):
        return reverse("poll_view", kwargs={"pk": self.object.poll.pk})

class ChoiceDeleteView(DeleteView):
    form_class = ChoiceForm
    model = Choice
    template_name = "choices/delete.html"

    def get_success_url(self):
        return reverse("choice_delete", kwargs={"pk": self.object.choice.pk})