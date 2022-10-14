from django.forms import ModelForm
from django.shortcuts import render
from myapp.models import ListData


class ListForm(ModelForm):
    class Meta:
        model = ListData
        fields = ['title', 'description', 'deadline', 'done']


def AllList(req):
    return render(req, 'myapp/TodoList.html', {
        'AllList': ListData.objects.all().order_by('deadline')
    })

def SearchList(req):
    q = req.GET['query']
    mydictionary = {
        "AllList" : ListData.objects.filter(title__contains=q)
    }
    return render(req,'myapp/TodoList.html',context=mydictionary)

def AddList(req):
    obj = ListData()
    obj.title = req.GET.get('title')
    obj.description = req.GET.get('description')
    obj.deadline = req.GET.get('deadline')
    obj.done = req.GET.get('done', False)
    if not obj.done:
        obj.done = False
        obj.save()
        mydictionary = {
            "AllList": ListData.objects.all()
        }
        return render(req, 'myapp/TodoList.html', context=mydictionary)

    else:
        obj.done = True
        obj.save()
        mydictionary = {
            "AllList": ListData.objects.all()
        }
        return render(req, 'myapp/TodoList.html', context=mydictionary)

def editList(req,id):
    obj = ListData.objects.get(id=id)
    mydictionary = {
        "title" : obj.title,
        "description" : obj.description,
        "deadline" : obj.deadline,
        "done": obj.done,
        "id" : obj.id
    }
    return render(req, 'myapp/editList.html', context=mydictionary)

def UpdateList(req,id):
    obj = ListData(id=id)
    obj.title = req.POST.get('title')
    obj.description = req.POST.get('description')
    obj.deadline = req.POST.get('deadline')
    obj.done = req.POST.get('done', False)
    if not obj.done:
        obj.done = False
        obj.save()
        mydictionary = {
            "AllList": ListData.objects.all()
        }
        return render(req, 'myapp/TodoList.html', context=mydictionary)

    else:
        obj.done = True
        obj.save()
        mydictionary = {
            "AllList": ListData.objects.all()
        }
        return render(req, 'myapp/TodoList.html', context=mydictionary)

def DeleteList(req,id):
    obj = ListData.objects.get(id=id)
    obj.delete()
    mydictionary = {
        "AllList" : ListData.objects.all()
    }
    return render(req,'myapp/TodoList.html',context=mydictionary)
