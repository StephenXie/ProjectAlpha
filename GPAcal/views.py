from django.shortcuts import render

# Create your views here.
def homeview(request):
    GPA = 0
    return render(request,"home.html",GPA)