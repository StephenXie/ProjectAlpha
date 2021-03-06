from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem


# Create your views here.
def todoView(request):
    all_todo_items = TodoItem.objects.all()
    # return HttpResponse("hello")
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
