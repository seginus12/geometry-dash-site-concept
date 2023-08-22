from django.http import HttpResponse
from django.shortcuts import render
from .models import Player
from django.views.decorators.cache import cache_page
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.conf import settings

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
def index(request):
    return render(request, "gd/mainpage.html")

def profile(request):
    return HttpResponse("Your geometry dash profile")

def top_hardest(request):
    return HttpResponse("Top 200 geometry dash hardest levels")

def rankings(request):
    players = Player.objects.all()
    return render(request, 'gd/rankings.html', {'players': players})