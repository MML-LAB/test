from django.shortcuts import render, HttpResponse

def homepage(request):
    return HttpResponse("Hello world")

def test (request):
    return render(request, "test.html")

def second(request):
    return HttpResponse("Second page")

def third(request):
    return HttpResponse("this is a third page")
