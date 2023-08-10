from django.urls import path
from basket.views import cart_upload

urlpatterns = [
    path("cart/upload",cart_upload,name="cart_upload_view"),
    
]