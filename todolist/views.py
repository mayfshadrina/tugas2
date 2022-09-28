from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import create_form

# Create your views here.
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_task = Task.objects.filter(user = request.user) #sesuai sama user yang lagi login
    context = {
    'list_task': data_task,
    'last_login': request.COOKIES['last_login'],
    }
    return render(request, 'todolist.html', context)

def create_task(request):
    if request.method == 'POST':
        form = create_form(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            Task.objects.create(title = title, description = description, date = datetime.datetime.now(), user = request.user)
            return redirect('todolist:show_todolist')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = create_form()
    context = {
        'form': form,
        }
    return render(request, 'create_task.html', context)

def delete(request, id):
  member = Task.objects.get(id=id)
  member.delete()
  return redirect('todolist:show_todolist')

def ubah(request, id):
  member = Task.objects.get(id=id)
  member.is_finished = not(member.is_finished)
  member.save()
  return redirect('todolist:show_todolist')