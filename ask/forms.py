from django import forms
from ask.models import Question


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'text', )