from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task 

# Create your views here.
def addTask(request):
    task = request.POST['task']
    Task.objects.create(
        task=task
    )
    return redirect('home')

def mark_as_done(request, pk):
    # use pk to get data and edit it
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True 
    task.save()
    # return HttpResponse(task)
    return redirect('home')

def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk) # gets the task based on the pk.
    task.is_completed = False # edit object
    task.save() # save object
    return redirect('home')

def edit_task(request, pk):
    return render(request, 'edit_task.html')