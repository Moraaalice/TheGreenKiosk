from django.shortcuts import render
from.forms import ProductAploadForm

# Create your views here.
def upload_product(request):
    if request.method == "POST":
        form = ProductAploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()


    else:
        form = ProductAploadForm()
    return render(request,"inventory/product_upload.html",{"form":form})




