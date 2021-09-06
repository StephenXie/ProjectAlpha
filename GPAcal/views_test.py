from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.views import View
from GPAcal.scripts import getGPA_w, getGPA_u, getMaxGPA
from rest_framework.decorators import api_view
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

# Create your views here.


def api_GPAcal(request):
    raw_GPA_u = raw_GPA_w = max_GPA = 4.0
    if request.method == "POST":
        print("SX")
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        classes = data.get("class_name")
        grades = data.get("grade")
        class_type = data.get("class_type")
        credit = data.get("credit")
        raw_GPA_w = getGPA_w(grades, class_type, credit)
        raw_GPA_u = getGPA_u(grades, credit)
        max_GPA = getMaxGPA(class_type)
    pct_u = (raw_GPA_u/4)*100
    pct_u = round(pct_u, 2)
    pct_w = (raw_GPA_w/max_GPA)*100
    pct_w = round(pct_w, 2)
    GPA_w = round(raw_GPA_w, 2)
    GPA_u = round(raw_GPA_u, 2)
    args = {"GPA_w": GPA_w, "GPA_u": GPA_u, "raw_GPA_w": raw_GPA_w, "raw_GPA_u": raw_GPA_u, "max_GPA": round(
        max_GPA, 2), "pct_u": pct_u, "pct_w": pct_w}
    return HttpResponse(json.dumps(args))
