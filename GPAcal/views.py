from django.shortcuts import render

# Create your views here.
def GPAcalview(request):
    GPA = 0
    return render(request,"GPAcal.html",GPA)