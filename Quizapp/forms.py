from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class RegisterFrom(UserCreationForm):

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter email-address",
            }
        )
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter password"}
        ),
        help_text=None,
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Confim password"}
        ),
        help_text=None,
    )

    class Meta:
        model = CustomUser
        fields = ["email", "password1", "password2"]


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter email-address",
            }
        )
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter password"}
        ),
    )


class QuestionsForm(forms.Form):
    def __init__(self, question_instance, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Define choices dynamically based on the question instance
        choices = [
            (question_instance.optionone, question_instance.optionone),
            (question_instance.optiontwo, question_instance.optiontwo),
            (question_instance.optionthree, question_instance.optionthree),
            (question_instance.optionfour, question_instance.optionfour),
        ]
        
        # Create a radio button group for the question
        self.fields['answer'] = forms.ChoiceField(
            choices=choices,
            widget=forms.RadioSelect,
            label="Choose your answer"
        )
        
        # Optionally set the initial value if it's already provided (e.g., correct answer)
        self.fields['answer'].initial = question_instance.answer
