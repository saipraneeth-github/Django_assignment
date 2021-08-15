from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Products

def display(request):
    context = {'product_list':Products.objects.all()}
    return render(request, 'display.html', context)

def create(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ProductForm()
        else:
            create = Products.objects.get(pk=id)
            form = ProductForm(instance=create)
        return render(request, 'create.html',{'form': form})
    else:
        if id == 0:
            form = ProductForm(request.POST)
        else:
            create = Products.objects.get(pk=id)
            form = ProductForm(request.POST,instance=create)
        if form.is_valid():
            form.save()
        return redirect('/view/')

def delete(request,id):
    create = Products.objects.get(pk=id)
    create.delete()
    return redirect('/view/')
