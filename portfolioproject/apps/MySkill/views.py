from django.shortcuts import render

# Create your views here.


def myskill(request):
    return render(request, 'myskill/myskill.html')
