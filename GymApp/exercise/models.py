from django.db import models

# Create your models here.

class MuscleGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Exercise(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, blank=True, null=True)
    muscle = models.ManyToManyField(MuscleGroup)
    isRepEx = models.BooleanField(default=True)


    def __str__(self):
        return self.name
    
class Reps(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    reps = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.exercise.name} - Reps: {self.reps}"
    

class CircuitWorkout(models.Model):
    exercises = models.ManyToManyField(Reps)
    rest = models.IntegerField()
    cicles = models.PositiveIntegerField()


class SeriesWorkout(models.Model):
    exercise = models.ForeignKey(Reps, on_delete=models.CASCADE)
    series = models.PositiveIntegerField()


class Traning(models.Model):
    name = models.CharField(max_length=200)
    workout = models.ManyToManyField(CircuitWorkout or SeriesWorkout) 
    


    