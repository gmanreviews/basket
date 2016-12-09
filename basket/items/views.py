from django.shortcuts import render
from django.http import HttpResponse
from .models import item
# Create your views here.
def index(request):
    return HttpResponse("You're viewing an item. I guess.")

def all_items(request):
    this_item = item.objects.all()
    return render(request, 'items/all.html', {'items': this_item})
