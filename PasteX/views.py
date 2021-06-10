from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import PasteXItem
from .scripts import b64
import hashlib
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def PasteXView(request, my_id=None):
    if my_id:  # Retrieve
        try:
            item = PasteXItem.objects.get(pk=my_id)
        except ObjectDoesNotExist:
            return render(request, '404.html')
        return render(request, "pastex.html", {'item': item, "language": item.language})
    if request.method == "POST":
        # add item to model and return id
        content = request.POST.get('content')
        new_id = b64(hashlib.sha256(bytes(content, 'utf8')
                                    ).hexdigest()).replace("=", "")[:21]
        language = request.POST.get('content_type')
        new_item = PasteXItem(content=content, id=new_id, language=language)
        new_item.save()
        url = request.build_absolute_uri
        return render(request, "pastex.html", {'item_id': new_id})
    # show html
    return render(request, "pastex.html")
