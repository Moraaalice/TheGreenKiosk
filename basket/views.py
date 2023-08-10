from django.shortcuts import render
from basket.forms import FormCart

# Create your views here.
def cart_upload(request):
    if request.method == "POST":
        form = FormCart(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    else:
        form = FormCart()
    return render(request,"basket/cart_upload.html",{"form":form})

            
                    