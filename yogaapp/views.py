from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def twohundred(request):
    return render(request, "200hrs.html")

def threehundred(request):
    return render(request, "300hrs.html")

def philosophy(request):
    return render(request, "philosophy.html")

def chakra(request):
    return render(request, "chakra.html")

def cosmic(request):
    return render(request, "cosmic.html")

def natal(request):
    return render(request, "natal.html")