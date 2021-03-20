from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem
from django.forms.models import model_to_dict
from django.utils.timezone import localtime
# Create your views here.
class item:
    def __init__(self,date,content,id_):
        self.date = localtime(date)
        self.content = content
        self.id = id_
def todoView(request):
    all_todo_items = TodoItem.objects.all()
    items = []
    for i in all_todo_items:
        items.append(item(i.date,i.content,i.id))

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
