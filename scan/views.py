from django.shortcuts import render

from django.http import request

from django.views.static import serve

from .camera import scanframe



def home(request):


    return render(request,"mainindex.html")


def scan(request):

    result=scanframe()
    context={"result":result}

    return render(request,"scan.html",context)