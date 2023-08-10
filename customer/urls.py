from django.urls import path
from.views import customer_detail, customer_list, customer_upload, edit_customer_view

urlpatterns = [
    path("customer/details",customer_upload,name="customer_details_view"),
    path("customers/list",customer_list,name="customers_list_view"),
    path("customer/<int:id>/",customer_detail,name="customer_detail_view"),
    path("customers/edit/<int:id>/",edit_customer_view,name="product_edit_view")
]