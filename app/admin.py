from django.contrib import admin

# Register your models here.
from .models import Category,Sub_Category,Product,Order,Contact_us,Brand

admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Contact_us)
admin.site.register(Brand)
