from django.shortcuts import render
from mywatchlist.models import MyWatchlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist(request):
    data_mywatchlist = MyWatchlist.objects.all()
    context = {
    'list_watchlist': data_mywatchlist,
    'nama': 'Mayfa Shadrina Siddi',
    'npm' : '2106634616'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data_mywatchlist = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")

def show_json(request):
    data_mywatchlist = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")
