from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView, View

from webapp.forms import AnswerForm
from webapp.models import Answer, Poll, Choice

class CreateAnswerView(CreateView):
    model = Answer
    form_class = AnswerForm
    template_name = "answers/create.html"

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        self.object = form.save(commit=False)
        self.object.poll = poll
        self.object.save()
        return redirect('poll_view', pk=poll.pk)

    def get_form_kwargs(self):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        answer = super().get_form_kwargs()
        answer['choice'] = Choice.objects.filter(poll_id=poll.pk)
        return answer

    def get_context_data(self, **kwargs):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        context = super().get_context_data(**kwargs)
        context['poll'] = poll
        return context