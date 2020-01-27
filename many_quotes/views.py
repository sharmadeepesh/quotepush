from django.shortcuts import render
import requests
import json
from random import seed
from random import randint
from get_random_quote.models import Quote

def many_quotes(request):
    if request.method == "POST":
        quote = Quote.objects.all()
        count = 10
        quotes = {}
        filename = "static/quotes.json"
        try:
            count = int(request.POST.get('count'))
        except ValueError:
            pass
        with open(filename, 'r+') as j:
            response = json.loads(j.read())
        while len(quotes) != count:
            value = randint(444503,506592)
            if (quote.filter(quote=response['data'][str(value)]['quote'])):
                quote_temp = quote.filter(quote=response['data'][str(value)]['quote'])
                quotes[quote_temp[0].quote] = quote_temp[0].author
            else:
                quote_temp = quote.create(quote=response['data'][str(value)]['quote'], author=response['data'][str(value)]['author'])
                quote_temp.save()
                quotes[quote_temp.quote] = quote_temp.author
        data = {
            'quotes' : quotes,
        }
        return render(request,'many_quotes/many_quotes.html',context=data)
    elif request.method == "GET":
        return render(request,"many_quotes/base.html")