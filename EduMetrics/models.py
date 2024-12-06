from django.db import models

class County(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class School(models.Model):
    name = models.CharField(max_length=200)
    county = models.ForeignKey(County, on_delete=models.CASCADE, related_name="schools")
    num_teachers = models.IntegerField()
    num_learners = models.IntegerField()
    has_electricity = models.BooleanField(default=False)
    has_infrastructure = models.BooleanField(default=False)

    def __str__(self):
        return self.name




