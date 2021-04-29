from django.db import models

# Create your models here.


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
    TEXT='T'
    SELECT_ONE ='O'
    SELECT_SET = 'S'
    QUESTION_TYPE_CHOICES=[
      (TEXT, 'Text' ),
      (SELECT_ONE, 'Select one'),
      (SELECT_SET, 'Select_set'),
    ]
    typeQ = models.CharField(
      max_length=1,
      choices=QUESTION_TYPE_CHOICES,
      default=TEXT
    )
    title = models.CharField(max_length=120)
    description = models.TextField()
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

    def __unicode__(self):
        """Returns a string representation of a choice."""
        return self.text

class Respondent(models.Model):

    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Answer(models.Model):
    respondent = models.ForeignKey(Respondent, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answerIs = models.TextField(null=True)
    def __str__(self):
        return self.answerIs