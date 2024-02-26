from django.db import models
from django.contrib.auth.models import User

''' 
Django has an ORM, it makes easier the use of a DB in our system. 
With the class Task, django is able to create a table named Task. 
Dajngo also created methos to create Tasks, update and delete. 
'''

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.title} -by {self.user.username}'
