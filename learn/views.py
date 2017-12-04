from django.shortcuts import render

# Create your views here.
def learn_home(request):
    return render(request, 'learn/home.html', {})