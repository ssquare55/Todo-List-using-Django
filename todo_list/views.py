from django.shortcuts import render,redirect
from .models import list
from .forms import listform
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = listform(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = list.objects.all()
            messages.success(request,('item added'))
            return render(request,'home.html',{'all_items':all_items})

    else:
        all_items = list.objects.all()
        return render(request,'home.html',{'all_items':all_items})

def about(request):
    return render(request,'about.html',{})

def delete(request,list_id):
    item = list.objects.get(pk=list_id)
    item.delete()
    messages.warning(request,('item Deleted'))
    return redirect('home')

def cross(request,list_id):
    item = list.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')

def uncross(request,list_id):
    item = list.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')

def edit(request,list_id):
    if request.method == 'POST':
        item = list.objects.get(pk=list_id)
        form = listform(request.POST or None,instance = item)

        if form.is_valid():
            form.save()
            messages.success(request,('item edited'))
            return redirect('home')

    else:
        items = list.objects.get(pk=list_id)
        return render(request,'edit.html',{'items':items})
