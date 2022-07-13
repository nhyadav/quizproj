from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from . import models
# Create your views here.


def home(request):
    return render(request, 'registration/home.html')


def register(request):
    msg = None
    form = forms.RegisterUser
    if request.method == 'POST':
        form = forms.RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Data has been added'
    return render(request, 'registration/register.html', {'form': form, 'msg': msg})


def categories(request):
    catData = models.QuizCategory.objects.all()
    return render(request, 'registration/category.html', {'data': catData})


@login_required
def category_questions(request, cat_id):
    category = models.QuizCategory.objects.get(id=cat_id)
    question = models.QuizQuestion.objects.filter(
        category=category).order_by('id').first()
    return render(request, 'registration/category-questions.html', {'question': question, 'category': category})


@login_required
def submit_answer(request, cat_id, quest_id):
    if request.method == 'POST':
        category = models.QuizCategory.objects.get(id=cat_id)
        question = models.QuizQuestion.objects.filter(
            category=category).order_by('id').first()
        return render(request, 'registration/category-questions.html', {'question': question, 'category': category})
    else:
        return HttpResponse('Method Not allowed!!')
