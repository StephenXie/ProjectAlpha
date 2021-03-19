from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from GPAcal.scripts import getGPA_w, getGPA_u
# Create your views here.
def GPAcal(request):
    GPA_u = GPA_w = 4
    if request.method == "POST":
        classes = request.POST.getlist("class_name")
        grades = request.POST.getlist("grade")
        class_type = request.POST.getlist("class_type")
        GPA_w = getGPA_w(grades,class_type)
        GPA_u = getGPA_u(grades,class_type)
    GPA_w = round(GPA_w,2)
    GPA_u = round(GPA_u,2)
    args = {"GPA_w":GPA_w, "GPA_u":GPA_u}
    return render(request,'gpa_cal.html',args)