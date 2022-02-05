from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from webapp.forms import AnswerForm
from webapp.models import Answer, Poll

class CreateAnswerView(CreateView):
    model = Answer
    template_name = 'answers/create.html'
    form_class = AnswerForm

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        answer = form.save(commit=False)
        answer.poll = poll
        answer.save()
        return redirect('poll_view', pk=poll.pk)

# def answer_create_view(request, pk):
#     if request.method == 'GET':
#         form = AnswerForm()
#         return render(request, 'answers/create.html', {"form":form})
#     else:
#         form = AnswerForm(data=request.POST)
#         if form.is_valid():
#             choice = form.cleaned_data.get('choice')
#             poll = form.cleaned_data.get('poll')
#             created_at = form.cleaned_data.get('created_at')
#             new_answer = Answer.objects.create(choice=choice,
#                                            poll=poll,
#                                            created_at=created_at,)
#             return redirect("poll_view", pk=new_answer.pk)
#         return render(request, "answers/create.html")
