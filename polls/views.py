from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from polls.models import Question,Choice


# Create your views here.

def index(request):
    last_question_list = Question.objects.all()
    print(last_question_list)
    return render(request, "polls/index.html", {
        "last_question_list": last_question_list})


def detail(request, question_id):
    questions: Question = get_object_or_404(Question, pk= question_id)
    return render(request, "polls/details.html", {
        "question": questions})


def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html",{"question":question})


def votes(request, question_id):
    question: Question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/details.html",{
            "question": question,
            "error_message": "No elegiste una respuesta"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:result", args=(question.id,)))
