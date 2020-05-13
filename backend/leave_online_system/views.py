from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import LeaveDate
from .forms import LeaveForm

# Create your views here.


def index(request):
    employee = LeaveDate.objects.all()
    return render(request, 'frontend/index.html', {'context': employee})

def register(request):
    
    if request.method == 'POST':        
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request, 'registration/register.html', context)

@login_required(login_url='/accounts/login/')
def logout_view(request):
    logout(request)
    return redirect('index')


@login_required(login_url='/accounts/login/')
def employee_list(request):
    context = {'leave_list': LeaveDate.objects.all()}
    return render(request, 'leave_register/leave_list.html', context)

@login_required(login_url='/accounts/login/')
def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = LeaveForm()  
        else:
            leave = LeaveDate.objects.get(pk=id)
            form = LeaveForm(instance=leave)
        return render(request, 'leave_register/employee_form.html', {'form': form})
    else:
        if id == 0:
            form = LeaveForm(request.POST)
        else:
            leave = LeaveDate.objects.get(pk=id)
            form = LeaveForm(request.POST, instance=leave)
        if form.is_valid():
            form.save()
        return redirect('/accounts/list')

def employee_delete(request, id):
    leave = LeaveDate.objects.get(pk=id)
    leave.delete()
    return redirect('/accounts/list')