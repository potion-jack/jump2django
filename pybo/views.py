from django.shortcuts import render

# Create your views here.
from .models import Question

# QuestionList
def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list':question_list}
    return render(request, 'pybo/question_list.html', context)