from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Task(models.Model):
    content= models.CharField(max_length=100)
    date= models.DateTimeField(auto_now_add=True)
    complete= models.BooleanField(default=False)
    add_by=models.ForeignKey(User,on_delete=models.CASCADE,default=None)


    class Meta:
        ordering=['-date']

    def __str__(self):
        return self.content

class todo(models.Model):
    task=models.CharField(max_length=200)
    user=models.ForeignKey(User, on_delete=models.CASCADE)