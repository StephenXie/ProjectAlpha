from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem
from django.forms.models import model_to_dict

# Create your views here.
def todoView(request):
    all_todo_items = TodoItem.objects.all()
    for i in all_todo_items:
        print(model_to_dict(i)['date'])
    return render(request, 'todo.html',
                  {'all_items': all_todo_items})


def addTodo(request):
    new_item = TodoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')


def deleteTodo(request, todo_id):
    delete_item = TodoItem.objects.get(id=todo_id)
    delete_item.delete()
    return HttpResponseRedirect('/todo/')
