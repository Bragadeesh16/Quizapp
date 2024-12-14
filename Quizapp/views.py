from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, redirect
from django.contrib import messages


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
    random_questions = Questions.objects.filter(
        questionsbank=questionBank
    ).order_by("?")

    # to redirect the use if he already took the test

    if Useranswer.objects.filter(question_bank=questionBank):
        return redirect("result", questionBank.id)

    answers = {}

    if request.method == "POST":
        for question in random_questions:
            selected_option = request.POST.get(
                f"question_{question.id}"
            )
            answers[question.id] = selected_option

        correct_answer_count = 0
        for id, answer in answers.items():
            ques = random_questions.get(id=id)
            correct_answer = ques.answer
            if answer == correct_answer:
                correct_answer_count += 1

        user_answer = Useranswer.objects.create(
            user=request.user,
            question_bank=questionBank,
            answers=answers,
            score=correct_answer_count,
        )
        user_answer.save()

        return redirect("result", questionBank.id)

    return render(
        request, "quiz.html", {"questions": random_questions}
    )


def result(request, pk):
    questionBank = QuestionBank.objects.get(id=pk)
    useranswer = Useranswer.objects.get(question_bank=questionBank,user = request.user)
    user_ans = useranswer.answers
    result_data = []

    for id, selected_answer in user_ans.items():
        question = Questions.objects.get(id=id)
        question_count = len(Questions.objects.filter(questionsbank = questionBank))
        correct_answer = question.answer
        is_correct = None
        if selected_answer == correct_answer:
            is_correct = selected_answer

        result_data.append(
            {
                "question": question.question,
                "selected_answer": selected_answer,
                "correct_answer": correct_answer,
                "is_correct": is_correct,
            }
        )
       
    return render(
        request,
        "result.html",
        {
            "useranswer": useranswer,
            "result_data": result_data,
            'total':question_count
        },
    )
