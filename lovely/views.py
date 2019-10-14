from django.shortcuts import render

def first(request):
    return render(request, 'lovely/first.html')


def second(request):
    return render(request, 'lovely/second.html')


def third(request):
    return render(request, 'lovely/third.html')
