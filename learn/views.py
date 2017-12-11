from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'learn/index.html')


def learn_home(request):
    return render(request, 'learn/home.html', {})


