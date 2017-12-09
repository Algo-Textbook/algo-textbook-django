from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Question


def question_list(request):
    questions = Question.objects.filter().order_by()
    return render(request, 'ask/question_list.html', {'questions': questions})


def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'ask/question_detail.html', {'question': question})

