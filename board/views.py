from django.shortcuts import render
from .models import Board
# Create your views here.
def index(request):
    b=Board.objects.all()
    context={
        "bset":b
    }
    return render(request,'board/index.html',context)