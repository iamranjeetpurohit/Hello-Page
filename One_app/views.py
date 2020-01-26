from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dict = {'insert_me':"Hello i am coming from One app index.html !"}
    return render(request,'One_app/index.html',context=my_dict)
