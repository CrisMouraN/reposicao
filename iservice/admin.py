from django.contrib import admin

from . import models


admin.site.register(models.User)
admin.site.register(models.CreditCard)
admin.site.register(models.Service)
admin.site.register(models.TypeService)



# Register your models here.
