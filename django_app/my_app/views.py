from django.shortcuts import render


def page(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')
