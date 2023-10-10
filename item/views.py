from django.shortcuts import render,redirect
from .models import items
from .form import itemform

# Create your views here.
def item_list(request):
    context = {'item_list':items.objects.all()}
    return render(request,"item/item_list.html",context)

def item_form(request, id=0):           #perform get and post requests#Insert and update
    if request.method=="GET":
        if id==0:
            form = itemform()
        else:
            Item = items.objects.get(pk=id)    

            form= itemform(instance=Item)
        return render(request,'item/item_form.html',{'form':form})
    else:
        if id == 0:
            form = itemform(request.POST)
        else:
            Item = items.objects.get(pk=id) 
            form = itemform(request.POST,instance=Item)   
        if form.is_valid():
            form.save()
        return redirect('/list')




def item_delete(request,id):
    Item=items.objects.get(pk=id)
    Item.delete()
    return redirect('/list')