
from django.forms import model_to_dict
from django.contrib import messages
from django.shortcuts import render
from Questionnaires.models import Questionnaire
import json

def index(request): 
    questionnaires = list(Questionnaire.objects.all())
    dumps = [model_to_dict(questionnaire) for questionnaire in questionnaires]
    dumps = json.dumps(dumps) 
    questionnaires = [questionnaire.title for questionnaire in questionnaires]
    
    if request.method == 'POST':
        data = request.POST.copy().dict()
        data.pop("csrfmiddlewaretoken")
        questionnaire = Questionnaire(**data)
        
        if questionnaire.title == "" or questionnaire.language == "" or questionnaire.description == "":
            messages.add_message(request, messages.ERROR, "Tietoa puuttuu!")
        
        elif len(list(Questionnaire.objects.filter(title=questionnaire.title))) != 0:
            messages.add_message(request, messages.ERROR, "Kysely on jo olemassa!")    
        else:
            questionnaire.save()
            messages.add_message(request, messages.SUCCESS, "Uusi kysely luotu!")
    return render(request, 'index.html', {'questionnaires' : dumps, 'list' : questionnaires})