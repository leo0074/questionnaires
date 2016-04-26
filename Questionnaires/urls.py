from django.conf.urls import url

from Questionnaires.views.index import index
from Questionnaires.views.question import question, browse
from Questionnaires.views.answer import answer

urlpatterns = [
    url(r'^$',index, name="index"),
    url(r'^question',question, name="question"),
    url(r'^browse',browse, name="browse"),
    url(r'^answer',answer, name="answer"),
]