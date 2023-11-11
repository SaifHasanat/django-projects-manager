from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL

class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
       return self.name

class ProjectStatus(models.IntegerChoices):
    PENDEING=1,"pending"
    COMPLETED=2,"completed"
    POSTPONED=3,"postponed"
    CANCELED=4,"canceled"


class Project(models.Model):
    title=models.CharField(max_length=250)
    description=models.TextField()
    created_at=models.TimeField(auto_now_add=True)
    updated_at=models.TimeField(auto_now=True)
    status=models.IntegerField(choices=ProjectStatus.choices,default=ProjectStatus.PENDEING)
    category=models.ForeignKey(Category,on_delete=models.PROTECT)
    user=models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    # عند حذف المستخدم تحذف المهام المتعلقة به ايضا

    def __str__(self):
        return self.title


class Task(models.Model):
    description=models.TextField()
    is_completed=models.BooleanField(default=False)
    project= models.ForeignKey(Project,on_delete=models.CASCADE)
    # عند حذف المشروع تحذف المهام المتعلقة به ايضا

    def __str__(self):
        return self.description


