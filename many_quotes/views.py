from django.shortcuts import render
import requests
import json
from random import seed
from random import randint

def many_quotes(request):
    count = 10
    if request.method == "POST":
        quotes = {}
        try:
            count = int(request.POST.get('count'))
        except ValueError:
            pass
        content = requests.get('https://programming-quotes-api.herokuapp.com/quotes').content
        response = json.loads(content)
        while len(quotes) != count:
            value = randint(0, 10)
            quotes[response[value]['en']] = response[value]['author']
        data = {
            'quotes' : quotes,
        }
        return render(request,'many_quotes/many_quotes.html',context=data)
    elif request.method == "GET":
        return render(request,"many_quotes/base.html")