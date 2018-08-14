from django.db import models

# Create your models here.
import datetime
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):

        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class FirstIndex(models.Model):
    title = models.CharField(max_length=20)
    def __str__(self):
        return self.title

class SecoundIndex(models.Model):
    subtitle = models.CharField(max_length=20)
    ancester_id = models.ForeignKey(FirstIndex, on_delete=models.CASCADE)
    def __str__(self):
        return self.subtitle

class ThirdIndex(models.Model):
    subsubtitle = models.CharField(max_length=20)
    ancester_id = models.ForeignKey(SecoundIndex, on_delete=models.CASCADE)
    content = models.CharField(max_length=2000, null = True)
    def __str__(self):
        return self.subsubtitle
