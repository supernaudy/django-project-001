from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import models, login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.utils import timezone
from .forms import TaskForm
from .models import Task

# Create your views here.

def index(request):
	if request.user.is_authenticated:
		return redirect('tasks')
	else:
		error = None
		if request.method == 'POST':
			try:
				if request.POST.get('password2'):
					#signup
					if request.POST['password1'] == request.POST['password2']:
						user = models.User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
						user.save()
					else:
						raise Exception('Password do not match !!!')
				else:
					#signin
					user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
					if not user:
						raise Exception('Username or password incorrect !!!')
				login(request, user)
				return redirect('tasks')
			except IntegrityError as e:
				error = 'User already exist !!!'
			except Exception as e:
				error = e.args[0]
		return render(request, 'home.html', {'error': error})

@login_required
def tasks(request):
	return render(request, 'task_list.html', {'tasks': Task.objects.filter(user=request.user)})

@login_required
def create_task(request):
	error = ''
	if request.method == 'POST':
		try:
			form = TaskForm(request.POST)
			new_task = form.save(commit=False)
			new_task.user = request.user
			new_task.save()
			return redirect('index')
		except ValueError:
			error = 'Invalid data !!'

	return render(request, 'task_form.html', {
		'form': TaskForm,
		'error': error,
	})

@login_required
def task_detail(request, task_id):
	error = ''
	task = get_object_or_404(Task, pk=task_id, user=request.user)

	if request.method == 'POST':
		try:
			form = TaskForm(request.POST, instance=task)
			form.save()
			return redirect('index')
		except ValueError:
			error = 'Value error !!!'

	return render(request, 'task_form.html', {
		'form': TaskForm(instance=task),
		'error': error,
	})

@login_required
def mark_as_done(request, task_id):
	task = get_object_or_404(Task, pk=task_id, user=request.user)
	if task:
		task.date_done = timezone.now()
		task.save()
	return redirect('index')

@login_required
def delete_task(request, task_id):
	task = get_object_or_404(Task, pk=task_id, user=request.user)
	if task:
		task.delete()
	return redirect('index')

@login_required
def signout(request):
	logout(request)
	return redirect('index')