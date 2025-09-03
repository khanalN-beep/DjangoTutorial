from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from polls.models import Question


# Create your views here.

def index(request):
    # return HttpResponse("Hello world, This is nirdesh khanal.")
    latest_question_list = Question.objects.all()
    template = loader.get_template('polls/index.html')
    context = {"latest_question_list":latest_question_list}
    # output = ','.join([q.question_text for q in latest_question_list])
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("This is the question details", question_id)

def result(request, question_id):
    return HttpResponse("This is the question details", question_id)

def vote(request, question_id):
    return HttpResponse("This is the vote to twh result", question_id)

# def index(request):


