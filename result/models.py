from django.db import models
from django.urls import reverse

# Create your models here.
class StudentResult(models.Model):
    name=models.CharField(max_length=200)
    school=models.CharField(max_length=200)
    roll=models.IntegerField()
    math=models.IntegerField()
    science=models.IntegerField()
    english=models.IntegerField()
    ssc=models.IntegerField()
    odia=models.IntegerField()
    sanskrit=models.IntegerField()
    total=models.IntegerField()
    div=models.CharField(max_length=200)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('result_detail',args=[str(self.id)])
