from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
# Create your views here.
def GPAcalView(request):
    
    return render(request,"gpa_cal.html")

def GPAcalPost(request):
    return 