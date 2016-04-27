from django.forms import model_to_dict
from Questionnaires.models import *
from django.contrib import messages
import json

from django.shortcuts import render

def question(request): 

    questionnaires = Questionnaire.objects.all()
    questionnaires = [questionnaire.title for questionnaire in questionnaires]
    
    if request.method == 'POST':
        data = request.POST.copy().dict()
        questionnaire = Questionnaire.objects.filter(title=data["questionnaire"])[0]
        question = Question.objects.create(type=data["type"], questionnaire=questionnaire, description= data["description"])
        if question.description == "":
            messages.add_message(request, messages.ERROR, "Kysymyksen kuvaus puuttui!")
            return render(request, 'question.html', {'list' : questionnaires})
        
        if question.type == "slider":
            question.min = data["min"]
            question.max = data["max"]
        
        question.save()
        messages.add_message(request, messages.SUCCESS, "Uusi kysymys luotu!")
        
    return render(request, 'question.html', {'list' : questionnaires})   


def browse(request):
    questionnaires = Questionnaire.objects.all()
    questionnaires = [questionnaire.title for questionnaire in questionnaires]    
    questions = list(Question.objects.all())
    
    dumps = []
    
    for question in questions:
        dictionary = model_to_dict(question)
        dictionary["questionnaire"] = question.questionnaire.title    
        dumps.append(dictionary)
    dumps = json.dumps(dumps)    
    
    if request.method == 'POST':
        data = request.POST.copy().dict()    
        if data["questionnaire"] == "empty":
            messages.add_message(request, messages.ERROR, "Valitse muokattava kysymys!")
        elif data["new_description"] == "":
            messages.add_message(request, messages.ERROR, "Anna uusi kuvaus!")            
        else:  
            #Creates old_question with data of current one then updates the question  
            question = Question.objects.filter(questionnaire=Questionnaire.objects.filter(title=data["questionnaire"]), description=data["question"])[0]
            old = Old_questions.objects.create(question=question, version=question.current_version, type=question.type, min=question.min, max=question.max, description=question.description)
            old.save()
            question.description = data["new_description"]
            question.current_version += 1
            question.save()
            messages.add_message(request, messages.ERROR, "Kysymys muokattu!")
            
    return render(request, 'browse.html', {'list' : questionnaires, 'questions' : dumps, 'amount' : len(questionnaires)})   