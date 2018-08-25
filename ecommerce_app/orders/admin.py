from django.contrib import admin

from .models import UserCheckout, UserAddress, Order

admin.site.register(UserCheckout)
admin.site.register(UserAddress)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user']
    list_filter = ('user',)
    search_fields = ('user', )
    
    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)