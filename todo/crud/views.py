from django.shortcuts import render
from .models import crud
from .forms import crudForm

# Create your views here.

def index(request):
    cruds = crud.objects.all()
    form = crudForm()

    context = {'cruds':cruds, 'form':form}

    return render(request, 'crud/list.html', context)