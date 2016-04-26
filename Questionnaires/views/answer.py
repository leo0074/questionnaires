
from django.forms import model_to_dict
from Questionnaires.models import *
from django.contrib import messages
import json
import datetime
from django.shortcuts import render

def answer(request): 
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
        data.pop("submit")
        data.pop("csrfmiddlewaretoken")
        uid = data.pop("uid")
        
        if uid == "":
            messages.add_message(request, messages.ERROR, "tunniste puuttuu")
        
        elif not data:
            messages.add_message(request, messages.ERROR, "Valitse kysely")
            
        else :
            for key in data:
                print(key)
                answer = Answer(answer=data[key], question=Question.objects.filter(description=key)[0], timestamp=datetime.datetime.now(), user_id=uid)
                answer.save()
                messages.add_message(request, messages.ERROR, "Kiitos vastauksestasi!")
        
    return render(request, 'answer.html', {'list' : questionnaires, 'questions' : dumps})       

