from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem
from django.forms.models import model_to_dict
from django.utils import timezone
import pytz
import tzlocal
# Create your views here.
class item:
    def __init__(self,date,content,id_):
        self.date = convert_to_localtime(date)
        self.utc_time = date
        self.content = content
        self.id = id_
def convert_to_localtime(utctime):
    tm = "%B %d,%Y %I:%M %p"
    utc = utctime.replace(tzinfo=pytz.UTC)
    localtz = utc.astimezone(timezone.get_current_timezone())
    return localtz.strftime(tm).lstrip("0").replace(" 0"," ")
def todoView(request):
    all_todo_items = TodoItem.objects.all()
    items = []
    for i in all_todo_items:
        items.append(item(i.date,i.content,i.id))
    print(tzlocal.get_localzone())
    return render(request, 'todo.html',
                  {'all_items': all_todo_items,'items':items})


def addTodo(request):
    new_item = TodoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')


def deleteTodo(request, todo_id):
    delete_item = TodoItem.objects.get(id=todo_id)
    delete_item.delete()
    return HttpResponseRedirect('/todo/')
