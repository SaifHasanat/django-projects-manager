from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=50)

class Project(models.Model):
    title=models.CharField(max_length=250)
    description=models.TextField()
    created_at=models.TimeField(auto_now=True)
    updated_at=models.TimeField(auto_now=True)
    status=models.CharField(max_length=50)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,choices=x)


class Task(models.Model):
    description=models.TextField()
    is_completed=models.BooleanField(default=True)
    project= models.ForeignKey(Project,on_delete=models.CASCADE)


