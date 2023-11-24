from django.shortcuts import render

# Create your views here.
def guru(request):
    return render(request,'guru.html')