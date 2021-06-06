from django.shortcuts import render
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
            results =Article.objects.filter(title__contains=q)

    return render(request, 'search.html',
                  {'form':form,
                   'q':q,
                   'results': results})
