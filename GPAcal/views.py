from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from GPAcal.scripts import getGPA
# Create your views here.
def GPAcal(request):
    GPA = 4
    if request.method == "POST":
        calculate_type = bool(request.POST.get("method_type"))
        classes = request.POST.getlist("class_name")
        grades = request.POST.getlist("grade")
        class_type = request.POST.getlist("class_type")
        GPA = getGPA(grades,class_type,calculate_type)
    args = {"GPA":GPA}
    return render(request,'gpa_cal.html',args)