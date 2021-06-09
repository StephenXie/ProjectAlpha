from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import LinkyItem
from .scripts import b64, generate_id
import random
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def LinkyView(request,my_id=None):
    if my_id:  # Retrieve
        try:
            item = LinkyItem.objects.get(pk=my_id)
        except ObjectDoesNotExist:
            return render(request, '404.html')
        return HttpResponseRedirect(item.content)
    if request.method == "POST":
        # add item to model and return id
        content = request.POST.get('content')
        new_id = generate_id()
        new_item = LinkyItem(content=content, id=new_id)
        new_item.save()
        return render(request, "linky.html", {'item_id': new_id})
    # show html
    return render(request, "linky.html")
