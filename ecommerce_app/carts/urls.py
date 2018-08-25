from django.conf.urls import  url
#from django.conf.urls.static import static
#from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.CartView.as_view() , name='cart'),
    
    #url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'),

]