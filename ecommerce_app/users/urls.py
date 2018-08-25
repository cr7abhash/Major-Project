from django.conf.urls import  url
#from django.conf.urls.static import static
#from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.login.as_view(), name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^newuserregister/$', views.new_user_creation, name='newuserregister'),
    url(r'^contact/$', views.contact_us, name='contact'),
    url(r'^aboutus/$', views.about_us, name='aboutus'),

    #url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'),

]