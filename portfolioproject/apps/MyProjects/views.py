from django.shortcuts import render

# Create your views here.


def myprojects(request):
    return render(request, 'myprojects/myprojects.html')
