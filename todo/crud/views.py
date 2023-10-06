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