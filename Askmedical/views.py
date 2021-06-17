from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import Article
from .forms import Search_Form, CreateUserForm

# Views are used to indicate what I will have in my page.

def registerPage(request):
    form= CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Askmedical account is created for ' + user)
            return redirect('login')

    context={'form':form}
    return render(request, 'accounts/register.html', context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('post_search')
        else:
            messages.info(request, 'Please check your credentials')

    context={}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


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

def detailpage(request, articleid):
    article = Article.objects.get(pk=articleid)

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

    return render(request, 'detailpage.html', context=demonstrate)

