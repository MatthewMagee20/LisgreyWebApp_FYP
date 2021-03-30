from django.shortcuts import render


def offline(request):
    return render(request, 'offline.html')


def error(request):
    return render(request, 'offline/404.html')
