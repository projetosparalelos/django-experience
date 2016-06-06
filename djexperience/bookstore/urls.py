from django.conf.urls import url
from .views import customer_list, customer_detail, customer_form

urlpatterns = [
    url(r'^customer_list', customer_list, name='customer_list'),
    url(r'^customer_detail/(?P<pk>\d+)/',
        customer_detail, name='customer_detail'),
    url(r'^customer/add/', customer_form, name='customer_add'),
]
