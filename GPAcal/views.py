from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from GPAcal.scripts import getGPA_w, getGPA_u, getMaxGPA
# Create your views here.
def GPAcal(request):
    GPA_u = GPA_w = max_GPA = 4.0
    if request.method == "POST":
        classes = request.POST.getlist("class_name")
        grades = request.POST.getlist("grade")
        class_type = request.POST.getlist("class_type")
        credit = request.POST.getlist("credit")
        GPA_w = getGPA_w(grades,class_type,credit)
        GPA_u = getGPA_u(grades,class_type,credit)
        max_GPA = getMaxGPA(class_type)
    pct_u = (GPA_u/4)*100
    pct_u = round(pct_u,2)
    pct_w = (GPA_w/max_GPA)*100
    pct_w = round(pct_w,2)
    GPA_w = round(GPA_w,2)
    GPA_u = round(GPA_u,2)
    args = {"GPA_w":GPA_w, "GPA_u":GPA_u, "max_GPA":round(max_GPA,2), "pct_u":str(pct_u)+"%", "pct_w":str(pct_w)+"%"}
    return render(request,'gpa_cal.html',args)