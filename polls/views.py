from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from polls.models import Question, Choice


# Create your views here.

# def index(request):
#     last_question_list = Question.objects.all()
#     print(last_question_list)
#     return render(request, "polls/index.html", {
#         "last_question_list": last_question_list})
#
#
# def detail(request, question_id):
#     questions: Question = get_object_or_404(Question, pk= question_id)
#     return render(request, "polls/details.html", {
#         "question": questions})
#
#
# def result(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html",{"question":question})

# Clase Base Views

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "last_question_list"

    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/details.html"


class ResultView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def votes(request, question_id):
    question: Question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/details.html", {
            "question": question,
            "error_message": "No elegiste una respuesta"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:result", args=(question.id,)))
