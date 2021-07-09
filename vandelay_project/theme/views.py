from django.shortcuts import render

def twindex(request):
    return render(request,'index.html')