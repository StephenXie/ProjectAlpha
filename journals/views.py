from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import JournalItem
from django.forms.models import model_to_dict
from django.utils import timezone
import pytz
# Create your views here.


class item:
    def __init__(self, date, content, id_):
        self.date = convert_to_localtime(date)
        self.utc_time = date
        self.content = content
        self.id = id_


def convert_to_localtime(utctime):
    tm = "%B %d,%Y %I:%M %p"
    utc = utctime.replace(tzinfo=pytz.UTC)
    localtz = utc.astimezone(pytz.timezone('America/Los_Angeles'))
    return localtz.strftime(tm).lstrip("0").replace(" 0", " ")


def journalView(request):
    all_journal_items = JournalItem.objects.all()
    items = []
    for i in all_journal_items:
        items.append(item(i.date, i.text, i.id))
    items.sort(key=lambda x: x.id)
    return render(request, 'journal.html',
                  {'all_items': all_journal_items, 'items': items, 'auth': request.user.is_authenticated})


def addJournal(request):
    if not request.user.is_authenticated:
        return render(request, '404.html')
    new_item = JournalItem(text=request.POST['text'])
    new_item.save()
    return HttpResponseRedirect('/journal/')


def deleteJournal(request, journal_id):
    if not request.user.is_authenticated:
        return render(request, '404.html')
    delete_item = JournalItem.objects.get(id=journal_id)
    delete_item.delete()
    return HttpResponseRedirect('/journal/')
