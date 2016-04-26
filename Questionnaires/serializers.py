from rest_framework import serializers

from Questionnaires.models import *

class QuestionnaireSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Questionnaire
        fields = ('id', 'title', 'language', 'description')
        
class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = ('id', 'type', 'version', 'questionnnaire', 'description')
        
class AnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Answer
        fields = ('id', 'question', 'answer', 'timestamp', 'user_id')        