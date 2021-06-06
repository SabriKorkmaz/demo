from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Article

# Views are used to indicate what I will have in my page.

def index(request):
    obj= Article.objects.all()
    context={
        "obj":obj,
    }
    return render(request, "results.html", context)

class MainpageView(TemplateView):
    template_name = 'home.html'

class SearchView(TemplateView):
    template_name = 'search.html'
