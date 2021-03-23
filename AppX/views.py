from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
# Create your views here.
def hi(request):
    return render(request,'AppX/hi.html')

def handler404(request, *args, **argv):
    response = render(request,'404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response
