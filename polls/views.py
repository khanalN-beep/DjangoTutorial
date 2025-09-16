from gc import get_objects

from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader

from polls.models import Question, Choice
from django.db.models import F
from django.urls import reverse
from django.views import generic

# Create your views here.


class IndexView(generic.ListView):
    queryset = Question.objects.all()
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, "polls/detail.html", {"question": question})
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# def vote(request, question_id):
#     # print("REQUEST:", request)
#     # print("REQUEST POST:", request.POST)
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST["choice"])
#     except (KeyError, Choice.DoesNotExist):
#         context = {"question": question, "error_message": "You didn't select a choice"}
#         return render(request, "polls/detail.html", context)
#     else:
#         selected_choice.votes = F('votes') + 1
#         selected_choice.save()
#         # messages.success(request, "Thanks for voting!")
#         # return HttpResponse("Successfully voted on this question")
#     # return HttpResponse("This is the vote to the result", question_id)
#         return HttpResponseRedirect(reverse("polls:result", args=(question.id,)))

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay voting form with error
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "You didn't select a choice.",
        })
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:result", args=(question.id,)))
