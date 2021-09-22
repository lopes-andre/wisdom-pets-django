from django.db import models

class Pet(models.Model):
    # Each choice is a two tuple, where the first value is what
    # is stored in the database, and the second value is used as
    # a display string in Forms and in Django Admin
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]

    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField('Vaccine', blank=True)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
