from django.shortcuts import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

def detail(request , question_id):
    question = get_object_or_404(Question,pk= question_id)
    return render(request, 'polls/details.html',{'question': question })


def index(request):
        latest_question_list =Question.objects.order_by('-pub_date')[:5]
        output = ', '.join([q.question_text for q in latest_question_list])
        return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("you're looking at question %s." %question_id)


def results(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html' , {'question': question})

def vote(request,question_id):
    question = get_object_or_404(question_id)
    try:
        Selected_choice = question.choice_set,get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request,'polls/detail.html',{'question': question, 'error_message': "You didn't select a choice.",})
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results' , args=(question.id,)))

class IndexView(generic.ListView):
    temlate_name = 'polls/index.html'
    context_object_name ='latest_question_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name ='polls/index.html'
    context_object_name='lastest_question_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
