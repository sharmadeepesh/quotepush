from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from random import seed
from random import randint
from get_random_quote.models import Quote


# Create your views here.
def get_random_quote(request):
    value = randint(0, 500)
    quote_render = Quote.objects.all()
    quote_to_render = quote_render[value].quote
    author_to_render = quote_render[value].author
    data = {
        'quote': quote_to_render,
        'author' : author_to_render,
    }
    return render(request,'random/get_random_quote.html',context=data)