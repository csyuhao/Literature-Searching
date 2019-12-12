from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

#from django.template import loader

from .models import LiteratureItem

# Create your views here.

def index(request):
    literature_list = LiteratureItem.objects.order_by('id')[:5]
    context = {
        'literature_list': literature_list,
    }
    return render(request, 'litsearch/index.html', context)


def details(request, lit_item_id):
    literature_item = get_object_or_404(LiteratureItem, pk=lit_item_id)
    context = {'literature_item': literature_item}
    return render(request, 'litsearch/details.html', context)