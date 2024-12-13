from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import JSONField


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(
        blank=True, null=True, max_length=30, unique=True
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        return super().save(*args, **kwargs)


@receiver(post_save, sender=CustomUser)
def save_username_when_user_is_created(
    sender, instance, created, *args, **kwargs
):
    if created:
        email = instance.email
        sliced_email = email.split("@")[0]
        instance.username = sliced_email
        instance.save()


class QuestionBank(models.Model):
    sessionname = models.CharField(max_length=50)

    def __str__(self):
        return self.sessionname


class Questions(models.Model):
    question = models.TextField()
    optionone = models.CharField(max_length=50)
    optiontwo = models.CharField(max_length=50)
    optionthree = models.CharField(max_length=50)
    optionfour = models.CharField(max_length=50)

    answer = models.CharField(max_length=50)

    questionsbank = models.ForeignKey(
        QuestionBank, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.question

class Useranswer(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    question_bank = models.ForeignKey(QuestionBank, on_delete=models.CASCADE) 
    answers = JSONField()
    score = models.IntegerField(default=0)