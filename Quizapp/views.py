from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, redirect
from django.contrib import messages
from django.forms import modelformset_factory


def register(request):
    form = RegisterFrom()
    if request.method == "POST":
        form = RegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            user = authenticate(email=email, password=password)
            print(user)
            login(request, user)
            messages.success(
                request, "your are signed in successfully"
            )
            return redirect("home")
    else:
        form = RegisterFrom()

    return render(request, "register.html", {"form": form})


def user_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        email = form.data["email"]
        password = form.data["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(
                request, "your are logged in successfully"
            )
            return redirect("home")
        else:
            form.add_error(None, _("invalid credentials"))
    return render(request, "login.html", {"form": form})


def signout(request):
    logout(request)
    messages.success(request, "you have been logged out")
    return redirect("home")


def home(request):
    sessions = QuestionBank.objects.all()
    return render(request, "home.html", {"sessions": sessions})


def quiz(request, pk):
    
    questionBank = QuestionBank.objects.get(id=pk)
    questions = Questions.objects.filter(
        questionsbank=questionBank
    ).order_by("?")
 
    question_forms = []
    question_order = []

    for question in questions:
        question_order.append(
            Questions.objects.get(question=question).id
        )
        form = QuestionsForm(question_instance=question)
        question_forms.append((question, form))

    if request.method == "POST":
        for question, form in question_forms:
            try:
                if form.is_valid():
                    selected_answer = form.cleaned_data['answer']
                    print(f"Answer selected for '{question.question}': {selected_answer}")
            except Exception as e:
                print(f"An error occurred: {e}")


            

    return render(request, "quiz.html", {'questions':questions,'question_forms': question_forms}) #"formset": formset,
