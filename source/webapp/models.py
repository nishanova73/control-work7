from django.db import models

# Create your models here.
from webapp.validators import MinLengthValidator
from django.db import models
from django.urls import reverse

# Create your models here.
class Poll(models.Model):
    question = models.TextField(max_length=200, null=False, blank=False, verbose_name="Description",
                                validators=(MinLengthValidator(7),))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date created")

    def __str__(self):
        return f"{self.pk}. {self.question}."

    class Meta:
        db_table = 'Polls'
        verbose_name = 'poll'
        verbose_name_plural = 'polls'


class Choice(models.Model):
    text = models.TextField(max_length=200, null=False, blank=False, verbose_name="Description",
                                validators=(MinLengthValidator(10),))
    poll = models.ForeignKey("webapp.Poll", on_delete=models.CASCADE,
                             related_name="choices",
                             verbose_name="Poll",
                             )

    def __str__(self):
        return f"{self.pk}. {self.text}."

    class Meta:
        db_table = 'Choices'
        verbose_name = 'choice'
        verbose_name_plural = 'choices'
