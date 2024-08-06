from django.contrib import admin
from . models import Product,Profile

class ProductAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","email","password")
admin.site.register(Product,ProductAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display=("username", "email","pass1")
admin.site.register(Profile,ProfileAdmin)

# Register your models here.
