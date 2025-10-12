from django.db import models

from django.contrib.auth.models import User

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    weight = models.FloatField()        
    reps = models.IntegerField()        
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} - {self.weight}kg x {self.reps} reps"
class Exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')
    name = models.CharField(max_length=100)
    sets = models.IntegerField(default=0)
    reps = models.IntegerField(default=0)
    weight = models.FloatField(default=0)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.sets} sets of {self.reps} reps"
