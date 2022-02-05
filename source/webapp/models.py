from django.db import models

# Create your models here.
from webapp.validators import MinLengthValidator
from django.db import models
from django.urls import reverse

# Create your models here.
class Poll(models.Model):
    question = models.TextField(max_length=200, null=False, blank=False, verbose_name="Question",
                                validators=(MinLengthValidator(7),))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date created")

    def get_absolute_url(self):
        return reverse('poll_view', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.pk}. {self.question}."

    class Meta:
        db_table = 'Polls'
        verbose_name = 'poll'
        verbose_name_plural = 'polls'


class Choice(models.Model):
    text = models.TextField(max_length=200, null=False, blank=False, verbose_name="Choice's text",
                                validators=(MinLengthValidator(10),))
    poll = models.ForeignKey("webapp.Poll", on_delete=models.CASCADE,
                             related_name="choices",
                             verbose_name="Poll",
                             )

    def get_absolute_url(self):
        return reverse('choice_view', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.pk}. {self.text}."

    class Meta:
        db_table = 'Choices'
        verbose_name = 'choice'
        verbose_name_plural = 'choices'


class Answer(models.Model):
    poll = models.ForeignKey("webapp.Poll", on_delete=models.CASCADE,
                             related_name="polls",
                             verbose_name="Poll",
                             )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    choice = models.ForeignKey("webapp.Choice", on_delete=models.CASCADE,
                             related_name="choices",
                             verbose_name="Choice",
                             )

    def __str__(self):
        return f"{self.pk}. {self.created_at}."

    class Meta:
        db_table = 'Answers'
        verbose_name = 'answer'
        verbose_name_plural = 'answers'