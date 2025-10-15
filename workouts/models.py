from django.db import models
from django.contrib.auth.models import User

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    notes = models.TextField(blank=True)
    name = models.CharField(max_length=100)
    muscle_group = models.CharField(
        max_length=50,
        choices=[
            ('Chest', 'Chest'),
            ('Back', 'Back'),
            ('Legs', 'Legs'),
            ('Arms', 'Arms'),
        
        ],
        default='Chest'
    )
    # weight = models.FloatField()
    # reps = models.IntegerField()
    # date = models.DateField(auto_now_add=True)
   

    def __str__(self):
      return f"{self.name} ({self.muscle_group}) - "


class Exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # name = models.CharField(max_length=100)
    sets = models.IntegerField(default=0)
    reps = models.IntegerField(default=0)
    weight = models.FloatField(default=0)
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.sets} sets of {self.reps} reps"
