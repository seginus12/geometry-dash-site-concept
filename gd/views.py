from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request, "gd/mainpage.html")

def profile(request):
    return HttpResponse("Your geometry dash profile")

def top_hardest(request):
    return HttpResponse("Top 200 geometry dash hardest levels")

def rankings(request):
    return render(request, 'gd/rankings.html')