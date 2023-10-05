from django.contrib import admin
from ecommapp.models import Contact, Producat,Orders, OrderUpdate

# Register your models here.
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderUpdate)