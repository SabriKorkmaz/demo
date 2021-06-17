from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Article
from .forms import Search_Form

# Views are used to indicate what I will have in my page.

def index(request):
    obj= Article.objects.all()
    context={
        "obj":obj,
    }
    return render(request, "results.html", context)

class MainpageView(TemplateView):
    template_name = 'home.html'

def Tagfeature(request):
    return render(request, 'tagpage.html')

def post_search(request):

    form = Search_Form()
    # q is the input that user typed
    q = ''
    results = []
    #we search the q the request GET
    if 'q' in request.GET:
        form = Search_Form(request.GET)
        #we put this for security issues
        if form.is_valid():
            q = form.cleaned_data['q']
            results =Article.objects.filter(title__icontains=q)

    return render(request, 'search.html',
                  {'form':form,
                   'q':q,
                   'results': results})

def detailpage(request, PM_id):
    article = Article.objects.get(pk=PM_id)
    #article = get_object_or_404(Article, pk=PM_id)

    demonstrate = {
                    "authors": article.authors,
                    "title": article.title,
                    "abstract": article.abstract,
                    "pmid": article.PM_id,
                    "keywords": article.keywords,
                    "tags": article.tags,
                    "pubdate": article.publication_date,
                    "article":article
                    }

    return render(request, 'detailpage.html', {'article': article})

