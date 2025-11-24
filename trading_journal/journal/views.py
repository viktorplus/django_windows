from django.shortcuts import render
from .models import Trade


def trades_list(request):
    trades = Trade.objects.all()
    return render(request, "trades_list.html", {"trades": trades})
