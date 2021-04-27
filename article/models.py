from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()

  def __str__(self):
    return self.name



class Article(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()
  body = models.TextField()
  author = models.ForeignKey('Author', related_name='articles', on_delete=models.CASCADE)

  def __str__(self):
    return self.title

class Poll(models.Model):
  timeOfBegin = models.DateTimeField()
  title = models.CharField(max_length=120)
  description = models.TextField()
  body = models.TextField()
  

class Question(models.Model):
  typeQ = models.IntegerField()
  title = models.CharField(max_length=120)
  description = models.TextField()
  bodyText = models.TextField()
  bodyJson = models.JSONField()
  polls = models.ManyToManyField(Poll)


    