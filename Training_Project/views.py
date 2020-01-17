from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
 
import json
import requests

from .forms import DictionaryForm

def oxford(request):
    search_result = {}
    if 'word' in request.GET:
        form = DictionaryForm(request.GET)
        if form.is_valid():
            search_result = form.search()
    else:
        form = DictionaryForm()
    return render(request, 'oxford.html', {'form': form, 'search_result': search_result})
    
def index(request):
    return render(request,'search.html')
   

def index2(request):
    return render(request,'home.html')


def topnews(request):
    keyword=request.GET.get('keyword','')
    if not keyword:
        return render(request,'news.html',{'keyword':''})
    else:
        main_url = "https://newsapi.org/v2/everything?q={}&from=2020-01-13&sortBy=popularity&apiKey=951eb8ae5c074f42a7b053d6067525ef".format(keyword)
  
        #fetching data in json format 
        news =requests.get(main_url).json() 
        
        # getting all articles in a string article 
        articles = news["articles"]        
        return render(request,'news.html',{'keyword':keyword,'articles':articles})

def show_dict(request):
    keyword=request.GET.get('keyword','')
    if not keyword:
        return render(request,'dictionary.html',{'keyword':''})
    else:
        main_url = "https://wordsapiv1.p.mashape.com/words/{}".format(keyword)
  
        # fetching data in json format 
        result =requests.get(main_url).json() 
        
        # getting all articles in a string article 
        articles = news["articles"]        
        return render(request,'news.html',{'keyword':keyword,'articles':articles})

def sms(request):
    return render(request,"sms.html")
