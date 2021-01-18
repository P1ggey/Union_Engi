from django.shortcuts import render
from articles.models import Articles
from django.views.generic import ListView, DetailView

# Create your views here.

#def article(request):
  #  list_articles = Articles.objects.all()
  #  context = {
  #      'list_articles': list_articles
   # }

   # template = 'article.html'

    #return render(request,template,context)

class article_list_view(ListView):
    model = Articles
    template_name = 'article.html'
    context_object_name = 'list_articles'

# class detail_list_view(ListView):
#     model = Articles
#     template_name = 'detail.html'
#     context_object_name = 'get_article'


def detail_page(request,id):
    get_article = Articles.objects.get(id=id)

    context = {
        'get_article':get_article
    }

    template ='detail.html'
    return render(request,template,context)