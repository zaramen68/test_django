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

class Question(models.Model):
  typeQ = models.IntegerField()
  title = models.CharField(max_length=120)
  description = models.TextField()
  # polls = models.OneToOneField(Poll, on_delete = models.SET_NULL, null=True)
  # bodyJson = models.JSONField(null=True)
  # polls = models.ManyToManyField(Poll)
  # polls = models.ForeignKey('Poll', related_name='questions', on_delete=models.CASCADE, null=True)
  def __str__(self):
    return self.description

class Poll(models.Model):
  timeOfBegin = models.DateTimeField('date publushed')
  title = models.CharField(max_length=120)
  description = models.TextField()
  body = models.TextField()
  questions = models.ManyToManyField(Question)
  def __str__(self):
    return self.title
  

class Choice(models.Model):
    """A poll choice object for use in the application views and repository."""
  poll = models.ForeignKey(Question, on_delete=models.CASCADE)
  text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

  def votes_percentage(self):
      """Calculates the percentage of votes for this choice."""
      total = self.poll.total_votes()
      return self.votes / float(total) * 100 if total > 0 else 0

  def __unicode__(self):
      """Returns a string representation of a choice."""
      return self.text

class Respondent(models.Model):

  name = models.CharField(max_length=200)
    def __str__(self):
      return self.name

class Answer(models.Model):
  respondent = models.ForeignKey('Respondent', related_name='name', on_delete=models.CASCADE)
  question = models.ForeignKey('Question', related_name='description', on_delete=models.CASCADE)
  answerIs = models.TextField(null=True)
  