from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from webapp.models import Poll, Choice, Answer

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = []
        widgets = {}

    def clean_question(self):
        if len(self.cleaned_data.get('question')) < 7:
            raise ValidationError(f"The question field must be more than 20 symbols!")
        return self.cleaned_data.get('question')

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('text',)

class AnswerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        choice = kwargs.pop('choice')
        super().__init__(*args, **kwargs)
        self.fields['choice'].queryset = choice

    class Meta:
        model = Answer
        exclude = ["poll", "created_at"]
        widgets = {"choice": forms.RadioSelect}

class PollDeleteForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ()


class ChoiceDeleteForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ()

