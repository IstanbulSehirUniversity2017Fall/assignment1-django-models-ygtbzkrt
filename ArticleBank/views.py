from django.shortcuts import render
from django.http import HttpResponse,Http404
from ArticleBank.models import *
# Create your views here.

def article(request, article_id):
    try:
        article = Articles.objects.get(pk=article_id)
        return HttpResponse('<h3><p>'+article.Text+'</p></h3>')
    except:
        raise Http404

def index(request):
    return HttpResponse('<h1> Welcome Article Bank </h1>')
