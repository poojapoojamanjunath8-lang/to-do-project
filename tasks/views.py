# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


# Display all tasks
def task_list(request):

    tasks = Task.objects.all().order_by('-created_at')

    return render(request, 'task_list.html', {
        'tasks': tasks
    })


# Add new task
def add_task(request):

    if request.method == 'POST':

        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('task_list')

    else:
        form = TaskForm()

    return render(request, 'task_form.html', {
        'form': form,
        'title': 'Add New Task'
    })


# Edit task
def edit_task(request, id):

    task = get_object_or_404(Task, id=id)

    if request.method == 'POST':

        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('task_list')

    else:
        form = TaskForm(instance=task)

    return render(request, 'task_form.html', {
        'form': form,
        'title': 'Edit Task'
    })


# Delete task
def delete_task(request, id):

    task = get_object_or_404(Task, id=id)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    return render(request, 'task_confirm_delete.html', {
        'task': task
    })


# Mark task as completed or pending
def toggle_task(request, id):

    task = get_object_or_404(Task, id=id)

    if request.method == 'POST':
        task.completed = not task.completed
        task.save()

    return redirect('task_list')
