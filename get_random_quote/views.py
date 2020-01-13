from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from random import seed
from random import randint


# Create your views here.
def get_random_quote(request):
    content = requests.get("https://programming-quotes-api.herokuapp.com/quotes/random").content
    response = json.loads(content)
    quote = response['en']
    author = response['author']
    data = {
        'quote': quote,
        'author' : author,
    }
    return render(request,'random/get_random_quote.html',context=data)