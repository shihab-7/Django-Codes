from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import TaskModel

# Create your views here.
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            # print(form.cleaned_data)
            return redirect ('homepage')
    else:
        form = TaskForm()
    return render(request, 'task.html', {'form': form})


# edit a task
def edit_task(request,id):

    task = TaskModel.objects.get(pk=id)
    task_form = TaskForm(instance=task)

    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect ('homepage')
    return render(request, 'task.html', {'form': task_form})


# delete a task
def delete_task(request,id):
    task = TaskModel.objects.get(pk=id)
    task.delete()
    return redirect ('homepage')