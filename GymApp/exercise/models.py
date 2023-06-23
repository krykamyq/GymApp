from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MuscleGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Exercise(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, blank=True, null=True)
    muscle = models.ManyToManyField(MuscleGroup)
    isRepEx = models.BooleanField(default=True)
    isAccepted = models.BooleanField(default=False)


    def __str__(self):
        return self.name
    
    def muscle_names(self):
        return ", ".join([muscle.name for muscle in self.muscle.all()])

    
class Reps(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    reps = models.PositiveIntegerField()
    rest = models.PositiveIntegerField()


    def __str__(self):
        return f"{self.exercise.name} - Reps: {self.reps} - Rest time: {self.rest}"
    

class Traning(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout = models.ManyToManyField(Reps)
  

    def __str__(self):
        return self.name
    
