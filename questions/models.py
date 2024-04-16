from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from datetime import datetime

from django.utils import timezone

from django import forms


##################################################################################################################
class Question_DB(models.Model):
    professor = models.ForeignKey(User, limit_choices_to={'groups__name': "Professor"}, on_delete=models.CASCADE, null=True)
    qno = models.AutoField(primary_key=True)
    question = models.CharField(max_length=100)
    optionA = models.CharField(max_length=100)
    optionB = models.CharField(max_length=100)
    optionC = models.CharField(max_length=100)
    optionD = models.CharField(max_length=100)
    answer = models.CharField(max_length=200)
    max_marks = models.IntegerField(default=0)

    def __str__(self):
        return f'Question No.{self.qno}: {self.question} \t\t Options: \nA. {self.optionA} \nB.{self.optionB} \nC.{self.optionC} \nD.{self.optionD} '


class QForm(ModelForm):
    class Meta:
        model = Question_DB
        fields = '__all__'
        exclude = ['qno', 'professor']
        widgets = {
            'question': forms.TextInput(attrs = {'class':'form-control'}),
            'optionA': forms.TextInput(attrs = {'class':'form-control'}),
            'optionB': forms.TextInput(attrs = {'class':'form-control'}),
            'optionC': forms.TextInput(attrs = {'class':'form-control'}),
            'optionD': forms.TextInput(attrs = {'class':'form-control'}),
            'answer': forms.TextInput(attrs = {'class':'form-control'}),
            'max_marks': forms.NumberInput(attrs = {'class':'form-control'}),
        }




##################################################################################################################

class Question_Paper(models.Model):
    professor = models.ForeignKey(User, limit_choices_to={'groups__name': "Professor"}, on_delete=models.CASCADE)
    qPaperTitle = models.CharField(max_length=100)
    questions = models.ManyToManyField(Question_DB)

    def __str__(self):
        return f' Question Paper Title :- {self.qPaperTitle}\n'


class QPForm(ModelForm):
    def __init__(self,professor,*args,**kwargs):
        super (QPForm,self ).__init__(*args,**kwargs) 
        self.fields['questions'].queryset = Question_DB.objects.filter(professor=professor)

    class Meta:
        model = Question_Paper
        fields = '__all__'
        exclude = ['professor']
        widgets = {
            'qPaperTitle': forms.TextInput(attrs = {'class':'form-control'})
        }




class Exam_Model(models.Model):
    professor = models.ForeignKey(User, limit_choices_to={'groups__name': "Professor"}, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    total_marks = models.IntegerField()
    question_paper = models.ForeignKey(Question_Paper, on_delete=models.CASCADE, related_name='exams')
    start_time = models.DateTimeField(default=timezone.now())
    end_time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name


class ExamForm(ModelForm):
    def __init__(self,professor,*args,**kwargs):
        super (ExamForm,self ).__init__(*args,**kwargs) 
        self.fields['question_paper'].queryset = Question_Paper.objects.filter(professor=professor)

    class Meta:
        model = Exam_Model
        fields = '__all__'
        exclude = ['professor']
        widgets = {
            'name': forms.TextInput(attrs = {'class':'form-control'}),
            'total_marks' : forms.NumberInput(attrs = {'class':'form-control'}),
            'start_time': forms.DateTimeInput(attrs = {'class':'form-control'}),
            'end_time': forms.DateTimeInput(attrs = {'class':'form-control'})
        }




