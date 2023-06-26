from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from .models import Exercise,Reps,Traning

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'description', 'muscle']
        
        
        
class ExerciseAdd(forms.ModelForm):
    class Meta:
        model = Reps
        fields = ['exercise', 'reps', 'rest']


class TraningForm(forms.ModelForm):
    class Meta:
        model = Traning
        fields = ['name']
       