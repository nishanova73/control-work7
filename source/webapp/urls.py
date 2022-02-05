from django.urls import path
from django.views.generic import RedirectView
from webapp.views import (IndexView,
                          CreatePollView,
                          PollView,
                          PollUpdateView,
                          PollDeleteView,
                          CreateChoiceView,
                          ChoiceUpdateView,
                          ChoiceDeleteView,
                          CreateAnswerView
                          # answer_create_view
                          )

urlpatterns = [
    path('', IndexView.as_view(), name="main_page"),
    path('polls/', RedirectView.as_view(pattern_name="main_page")),
    path('poll/create_poll/', CreatePollView.as_view(), name="poll_add"),
    path('poll_view/<int:pk>/', PollView.as_view(template_name="polls/view.html"), name="poll_view"),
    path('poll_view/<int:pk>/update/', PollUpdateView.as_view(), name="poll_update"),
    path('poll_view/<int:pk>/delete/', PollDeleteView.as_view(), name="poll_delete"),
    path('poll/<int:pk>/choice/add/', CreateChoiceView.as_view(), name="poll_choice_create"),
    path('poll/<int:pk>/answer/add/', CreateAnswerView.as_view(), name="poll_answer_create"),
    path('poll/<int:pk>/choice/update/', ChoiceUpdateView.as_view(), name="choice_update"),
    path('poll/<int:pk>/choice/delete/', ChoiceDeleteView.as_view(), name="choice_delete"),
]