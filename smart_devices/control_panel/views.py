from django.shortcuts import render
from .models import ongoing_task
from django.http import JsonResponse
# Create your views here.

def main(request):
    return render(request,"index.html")

def ongoing_task_view(request):
    obj = list(ongoing_task.objects.all())
    task,status = [],[]
    for i in obj:
        task.append(i.task)
        status.append(i.status)
    return JsonResponse({'task':task,'status':status})
