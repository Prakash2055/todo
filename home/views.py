from multiprocessing import context
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

@login_required
def home(request):
    if request.user.is_authenticated:
        todo=Task.objects.filter(add_by=request.user.id)
        # todo=Task.objects.all()
        # todo= Task.objects.filter()  
        count_todos= todo.count()
        completed_todo = Task.objects.filter(complete=True)
        count_completed_todo= completed_todo.count()
        count_uncompleted_todo= count_todos - count_completed_todo

        if request.method== 'POST':
            form= Task_form(request.POST)
            if form.is_valid():
                form.save(commit=False).add_by = request.user
                form.save()
                return redirect('home')
        else:
            form= Task_form

        todo=Paginator(Task.objects.filter(add_by=request.user.id),4)
        page=request.GET.get('page')
        try:
            todo=todo.page(page)
        except PageNotAnInteger:
            todo=todo.page(1)
        except EmptyPage:
            todo= todo.page(todo.num_pages)

        context={
            'todo': todo,
            'form': form,
            'count_todos':count_todos,
            'count_completed_todo':count_completed_todo,
            'count_uncompleted_todo':count_uncompleted_todo,
            'completed_todo':completed_todo,
            # 'add_by':add_by
        }
        
        return render(request, 'index.html',context)

        
    
    
def update(request, pk):
    todo=Task.objects.get(id=pk)
    if request.method== 'POST':
        form= UpdateTaskForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')

    else: 
        form= UpdateTaskForm(instance=todo)
        context={
            'form': form,
            'todo': todo,
            
        }

    return render(request, 'update.html', context)


def delete(request,pk):
    todo=Task.objects.get(id=pk)
    if todo.add_by == request.user:
        if request.method== 'POST':
            todo.delete()
            return redirect ('home')
        return render(request, 'delete.html')
    else:
        messages.error(request, 'error')
        return redirect('home')

    

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method== 'POST':
            username = request.POST['username']
            email= request.POST['email']
            password= request.POST['psw1']
            confirm_password= request.POST['psw2']
            if password!=confirm_password:
                messages.error(request, 'password does not match')
                return redirect(register)
            if password==confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'User Name is eixst')
                    return redirect(register)


                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email exits')
                    return redirect(register)
                else:
                    new_user= User.objects.create_user(username, email, password)
                    username=username
                    new_user.set_password(password)
                    new_user.save()
                return redirect('login')  
        
        return render(request, 'register.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['psw1']
            user = authenticate(request, username = username, password = password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, "Login successfully!")
                return redirect('home',)
            else:
                messages.info(request, f'account done not exit plz sign in')
        return render(request, 'login.html')

@login_required
def logout(request):
    auth.logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('login')




