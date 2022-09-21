from django.shortcuts import render
from mywatchlist.models import MyWatchlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist(request):
    data_mywatchlist = MyWatchlist.objects.all()
    data_true = MyWatchlist.objects.filter(watched = True)
    data_false = MyWatchlist.objects.filter(watched = False)
    
    lebih_banyak = 'Selamat, kamu sudah banyak menonton!'
    lebih_dikit = 'Wah, kamu masih sedikit menonton!'
    
    if len(data_true) > len(data_false):
        ucapan = lebih_banyak
    else:
        ucapan = lebih_dikit
        
    context = {
    'list_watchlist': data_mywatchlist,
    'nama': 'Mayfa Shadrina Siddi',
    'npm' : '2106634616',
    'watch_tf' : ucapan
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data_mywatchlist = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")

def show_json(request):
    data_mywatchlist = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")
