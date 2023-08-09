from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render

# from django.template import loader

from .models import Question

# second view w/ render() shortcut

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
      "latest_question_list": latest_question_list
      }
    return render(request, "polls/index.html", context)

# second index view
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("polls/index.html")
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

# first index view

# def index(request):
#   print('request: ', request)
#   latest_question_list = Question.objects.order_by("-pub_date")[:5]
#   output = ", ".join([q.question_text for q in latest_question_list])
#   return HttpResponse(output, request)

# shortcut detail

def detail (request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, "polls/detail.html", {"question": question})

# first detail

# def detail(request, question_id):
#   try:
#     question = Question.objects.get(pk=question_id)
#   except Question.DoesNotExist:
#     raise Http404("Question does not exist")
#   return render(request, "polls/detail.html", question)

def results(request, question_id):
  response = "You're looking at the result of question %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  response = "You're voting on question %s."
  return HttpResponse(response % question_id)
