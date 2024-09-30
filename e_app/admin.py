from django.contrib import admin

from e_app import models

# Register your models here.
admin.site.register(models.Login_view)
admin.site.register(models.Customer)
admin.site.register(models.Seller)
admin.site.register(models.Product)
admin.site.register(models.Buy)
admin.site.register(models.Cart)