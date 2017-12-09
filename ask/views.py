from django.shortcuts import render
from django.utils import timezone
from .models import Question


def question_list(request):
    questions = Question.objects.filter().order_by()
    return render(request, 'ask/question_list.html', {'questions': questions})
