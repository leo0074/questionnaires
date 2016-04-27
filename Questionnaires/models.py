from django.db import models

class Questionnaire(models.Model):
    title = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

class Question(models.Model):
    current_version = models.IntegerField(default=1)
    type = models.CharField(max_length=100)
    min = models.IntegerField(default=0)
    max = models.IntegerField(default=0)
    questionnaire = models.ForeignKey('Questionnaire', on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)    

#Storage for old versions of Questions
class Old_questions(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    version = models.IntegerField()
    type = models.CharField(max_length=100)
    min = models.IntegerField(default=0)
    max = models.IntegerField(default=0)
    description = models.CharField(max_length=1000)      

class Answer(models.Model):
    answer = models.CharField(max_length=100)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    user_id = models.IntegerField()
    