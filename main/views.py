from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    
    if ls in response.user.todolist.all():
    
        if response.method == "POST":
            print(response.POST)
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete= True
                    else:
                        item.complete= False
                    item.save()
            
            elif response.POST.get("newItem"):
                txt = response.POST.get("new")
                ls.item_set.create(text=txt, complete=False)
                
            elif response.POST.get("clear"):
                ls.item_set.all().delete()
                
        
        return render(response, "main/list.html", {"ls":ls})
    return render(response, "main/view.html", {})

def home(response): #home page
    return render(response, "main/home.html", {}) #pass variables into dictionary with {}

def create(response): #form page
    if response.method == "POST": #Post is used for forms that are secrtive, sensitive info, get is for non secretivie info
        form = CreateNewList(response.POST)
        
        if form.is_valid(): #this will only work if there is valid input in the data field
            n = form.cleaned_data["name"] #this will unencrypt the data
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)
            
        return HttpResponseRedirect("/%i" %t.id)
        
    else:
        form = CreateNewList()
        
    return render(response, "main/create.html", {"form":form})

def view(response):
    return render(response, "main/view.html", {})