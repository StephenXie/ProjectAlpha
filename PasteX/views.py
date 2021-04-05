from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import PasteXItem
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def PasteXView(request):
    my_id = request.GET.get("q")
    if my_id: # Retrieve
        try:
            item = PasteXItem.objects.get(pk=int(my_id))
        except ObjectDoesNotExist:
            return render(request,'404.html')
        return render(request,"pastex.html",{'item':item})
    elif request.method == "POST":
        # add item to model and return id
        new_item = PasteXItem(content=request.POST.get('content'))
        new_item.save()
        url = request.build_absolute_uri
        print(str(url))
        return render(request,"pastex.html",{'item_id':new_item.id})
    else:
        # show html
        return render(request,"pastex.html")