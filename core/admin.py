from django.contrib import admin
from core.models import Que, Store
# Register your models here.


class StoreAdmin(admin.ModelAdmin):
    pass

class QueAdmin(admin.ModelAdmin):
    pass

admin.site.register(Que, QueAdmin)
admin.site.register(Store, StoreAdmin)