
from django.db import models

# Create your models here.


class QuizCategory(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField()
    image = models.ImageField(upload_to='bat_imgs/')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class QuizQuestion(models.Model):
    category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
    question = models.TextField()
    option_1 = models.CharField(max_length=250)
    option_2 = models.CharField(max_length=250)
    option_3 = models.CharField(max_length=250)
    option_4 = models.CharField(max_length=250)
    level = models.CharField(max_length=120)
    time_limit = models.IntegerField()
    right_option = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.question
