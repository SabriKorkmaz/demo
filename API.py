
import os
import django
import numpy,re
import datetime

#In order to get database and other settings of the project for my script
os.environ.setdefault("DJANGO_SETTINGS_MODULE","AskMedicalProject.settings")
django.setup()

#imported the Entrez from Bio which I extensively studied the documents of it
from Bio import Entrez
from Askmedical.models import Article
from Askmedical.models import Sentence

#In order to divide the abstract information to sentencs I used NLTK.
# You can see futher explanation below.
import nltk.data

def searchforID(searcTerm, size):
    Entrez.email = 'kural.kenan@icloud.com'
    handle = Entrez.esearch(db='pubmed',term=searcTerm,retmax=str(size),retmode='xml')
    results_id = Entrez.read(handle)
    return results_id

def searchforArticleDetails(ListofIDs):
    IDs = ','.join(ListofIDs)
    Entrez.email = 'kural.kenan@icloud.com'
    handle = Entrez.efetch(db='pubmed', retmode='xml',id=IDs)
    article_results = Entrez.read(handle)
    return article_results
nltk.download('punkt')
pickle_det = nltk.data.load('tokenizers/punkt/english.pickle')
#This tokenizer divides a text into a list of sentences,
# by using an unsupervised algorithm to build a model for abbreviation words,
# collocations, and words that start sentences.

def DatabasePopulationforArticles(articles):
    for articleVar in articles:
        #Here I am getting the title, PM id and abstract by using XML tags.
        title = articleVar['MedlineCitation']['Article']['ArticleTitle']
        PM_id = articleVar['MedlineCitation']['PMID']
        #Here I define an empty list to divide the abstract into a list of sentences.
        listofSentences= []
        try:
            listofAbstracts = articleVar['MedlineCitation']['Article']['Abstract']['AbstractText']
            for sentence in listofAbstracts:
                #I use punkt to tokenize my sentences.
                sentences_var = pickle_det.tokenize((sentence).strip())
                for sentences_var in sentences_var:
                        listofSentences.append(sentences_var)
        except:
            pass
        #Here I merge the sentences I have into an abstract.
        abstract = (' '.join(listofSentences)).strip()

        #I perform the similar tasks for the keywords as well.
        keywords =""
        try:
            listofKeywords = articleVar['MedlineCitation']['KeywordList']
            for keyword in listofKeywords[0]:
                keywords += (str(keyword) + "; ")
        except:
            pass
        try:
            authors =""
            listofAuthors = articleVar['MedlineCitation']['Article']['AuthorList']
            for author in listofAuthors:
                authors += (str(author['ForeName']) + " " + str(author['LastName'] + ";"))
            authors=authors.strip(";")
        except:
            pass

        pubdate = ""
        try:

            pubdatelist= articleVar['PubmedData']['History']
            pubdate = pubdatelist[0]['Year'] + "-" + pubdatelist[0]['Month'] + "-" + pubdatelist[0]['Day']
      #      print("İlk tarih" + pubdate)
            pubdate = datetime.datetime.strptime(pubdate, '%Y-%m-%d %H:%M')
     #       print("İlk tarih" + pubdate)
        except:
            pass

        article = Article(abstract= abstract,title=title, PM_id=PM_id, keywords=keywords, authors=authors, publication_date=pubdate)
        article.save()

        sentence_var = title
        sentence_var = Sentence(article=article,type='title',sentence=sentence_var)
        sentence_var.save()

        for sentence_var in listofSentences:
            sentence_var = Sentence(article=article,type='abstract',sentence=sentence_var)
            sentence_var.save()


def Populate(searchTerm,totalSize,fetchSize):
    gathered_ids = Article.objects.values_list("PM_id",flat=True)
    tempValue = searchforID(searchTerm, totalSize)
    tempValue = tempValue['IdList']
    IdsofArticles = numpy.setdiff1d(tempValue,gathered_ids)

    TotalnumberofArticles = len(IdsofArticles)
    NumforFetch = int(TotalnumberofArticles/fetchSize)

    if(TotalnumberofArticles == 0):
        return

    for fetch_index in range(0,NumforFetch):
        article_start_index = fetch_index*fetchSize
        ids_to_fetch = IdsofArticles[article_start_index:article_start_index+fetchSize]
        print("Downloading "+ str(fetchSize)+" articles out of "+str(TotalnumberofArticles)+" articles")
        temp2 = searchforArticleDetails(ids_to_fetch);
        articles = temp2['PubmedArticle']
        DatabasePopulationforArticles(articles)

    if(TotalnumberofArticles % fetchSize == 0):
        return
    print("Downloading last " + str(TotalnumberofArticles % fetchSize) + " articles out of " + str(TotalnumberofArticles) + " articles")
    temp2 = searchforArticleDetails(IdsofArticles[NumforFetch*fetchSize:TotalnumberofArticles]);
    articles = temp2['PubmedArticle']
    DatabasePopulationforArticles(articles)

Populate("influenza",100, 200)

