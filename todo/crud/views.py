from django.shortcuts import render
from .models import crud
# Create your views here.

def index(request):
    cruds = crud.objects.all()
    context = {'cruds':cruds}

    return render(request, 'crud/list.html', context)