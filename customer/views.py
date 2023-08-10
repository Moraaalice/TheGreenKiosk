from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from customer.forms import FormName
from customer.models import Customer

# Create your views here.
def customer_upload(request):
    if request.method == "POST":
        form = FormName(request.POST, request.FILES)
        if form.is_valid():
            form.save()        
    else:
        form = FormName()
    return render(request,"inventory/customer_upload.html",{"form":form})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request,"inventory/customer_list.html",{"customers":customers})


def customer_detail(request,id):
    customer = Customer.objects.get(id = id)
    return render(request,"inventory/customer_detail.html",{"customer":customer})

def edit_customer_view(request,id):
    customer = Customer.objects.get(id = id)
    if request.method == "POST":
        form = FormName(request.POST,instance=customer)
        if form.is_valid:
            form.save()
            return redirect("customer_detail_view",id = customer.id)
    else:
        form = FormName(instance=customer)
    return render(request,"inventory/edit_customer.html",{"form":form})




