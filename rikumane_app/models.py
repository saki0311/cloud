
from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Company(models.Model):
    URL = models.CharField(max_length=100)
    CompanyName = models.CharField(max_length=100)
    LoginId = models.CharField(max_length=100)
    def __str__(self):
        return '<{0}>'.format(self.CompanyName)

class Event(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    EventName = models.CharField(max_length=100)
    EventStart = models.DateTimeField()
    EventEnd = models.DateTimeField()
    def __str__(self):
        return '<{0}>'.format(self.EventName)