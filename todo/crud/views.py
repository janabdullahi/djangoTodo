from django.shortcuts import render, redirect
from .models import crud
from .forms import crudForm

# Create your views here.

def index(request):
    cruds = crud.objects.all()
    form = crudForm()

    if request.method == 'POST':
        form = crudForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'cruds':cruds, 'form':form}
    return render(request, 'crud/list.html', context)

def update(request,pk):
    cruds = crud.objects.get(id=pk)
    form = crudForm(instance=cruds)

    if request.method == 'POST':
        form = crudForm(request.POST,instance=cruds)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form':form}
    return render(request, 'crud/update.html', context)

def delete(request,pk):
    item = crud.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'crud/delete.html',context)