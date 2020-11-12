from django.shortcuts import render, redirect
from django.http import *
from .models import *
from .forms import *


def index(request):
    t = Task.objects.all()
    form = Taskform()

    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'t': t, 'form': form}
    return render(request, 'task/list.html', context)


def updatetask(request, pk):
    t = Task.objects.get(id=pk)
    form = Taskform(instance=t)
    if request.method == 'POST':
        form = Taskform(request.POST, instance=t)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {"form": form}
    return render(request, 'task/update_task.html', context)


def deletetask(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item': item}
    return render(request, 'task/delete.html', context)
