from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from carts.views import ItemCountView
from orders.views import OrderList, CheckoutView, UserAddressCreateView, CheckoutFinalView, business_analysis, send_offer_email

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('products.urls')),
    url(r'^products/', include('products.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^carts/', include('carts.urls')),
    url(r'^cart/count/$', ItemCountView.as_view(), name='item_count'),
    url(r'^checkout/$', CheckoutView.as_view(), name='checkout'),
    url(r'^checkout/final/$', CheckoutFinalView.as_view(), name='checkout_final'),
    url(r'^checkout/address/$', UserAddressCreateView.as_view(), name='user_address_create'),
    url(r'^orders/$', OrderList.as_view(), name='orders'),
    url(r'^analysis/$', business_analysis, name='analysis'),
    url(r'^sendoffer/$', send_offer_email.as_view(), name='send_offer'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
