from django.conf.urls import  url
#from django.conf.urls.static import static
#from django.contrib import admin
from . import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    #url(r'^$', views.testcontroller , name='testcontroller'),
    url(r'^(?P<pk>\d+)/$', views.ProductDetailView.as_view(), name='product_detail'),
    url(r'^$', views.ProductListView.as_view(), name='products'),
    url(r'^search$', views.product_search, name='search'),
    #url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'),
    url(r'^api/$', views.ProductsListAPI.as_view(), name = "productsrest"),

]

urlpatterns = format_suffix_patterns(urlpatterns)