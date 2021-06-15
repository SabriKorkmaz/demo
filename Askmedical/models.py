from django.db import models

# Create your models here.

class Article(models.Model):
    abstract = models.TextField(null=True)
    PM_id = models.IntegerField(primary_key=True)
    title = models.TextField(null=True)
    keywords = models.TextField(null=True)
    authors = models.TextField(null=True)
    publication_date = models.DateField(null=True)

    def __str__(self):
        return str(self.PM_id)

class Sentence(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    type = models.TextField()
    sentence = models.TextField()

    def __str__(self):
        return self.sentence

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


