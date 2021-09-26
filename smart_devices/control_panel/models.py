from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.
class ongoing_task(models.Model):
    task = models.TextField(default="n/a")
    status = models.CharField(max_length=1)

class coffee_recipei(models.Model):
    name = models.CharField(max_length=20)
    powder = models.IntegerField(max_length=2)
    sugar = models.IntegerField(max_length=2)
    water = models.IntegerField(max_length=4)
    milk = models.IntegerField(max_length=4)
    temperature = models.IntegerField(max_length=3)
    mixer = models.IntegerField(max_length=4)

class coffee_logs(models.Model):
    coffee = models.ForeignKey(coffee_recipei,on_delete=models.CASCADE)
    powder = models.BooleanField(default=False)
    sugar = models.BooleanField(default=False)
    water = models.BooleanField(default=False)
    milk = models.BooleanField(default=False)
    temperature = models.BooleanField(default=False)
    mixer = models.BooleanField(default=False)
    status = models.BooleanField(default=False)

class machine_info(models.Model):
    name = models.CharField(max_length=20)
    ip = models.CharField(max_length=15)
    status = models.BooleanField(default=False)


class machine_log(models.Model):
    machine = models.ForeignKey(machine_info,on_delete=models.CASCADE)
    task_id = models.ForeignKey(coffee_logs,on_delete=models.CASCADE,null=True)
    task = models.CharField(max_length=20)
    value = models.IntegerField(max_length=4)
    status = models.BooleanField(default=False)

class machine_tasks(models.Model):
    machine = models.ForeignKey(machine_info,on_delete=models.CASCADE)
    task = models.CharField(max_length=20)
