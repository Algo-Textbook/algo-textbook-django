from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'learn/index.html')


def learn_home(request):
    return render(request, 'learn/home.html', {})


def group_activity(request):
    return render(request, 'learn/activity.html', {})


def u1_definition(request):
    return render(request, 'understand/u1_definition.html', {})


def u2_computer(request):
    return render(request, 'understand/u2_computer.html', {})


def u3_importance(request):
    return render(request, 'understand/u3_importance.html', {})


def u4_conditions(request):
    return render(request, 'understand/u4_conditions.html', {})


def u5_practice(request):
    return render(request, 'understand/u5_pratice.html', {})


def u6_test(request):
    return render(request, 'understand/u6_test.html', {})

