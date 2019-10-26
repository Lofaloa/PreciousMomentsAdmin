from django.contrib import admin

from .models import Glass
from .models import Supplier
from .models import Material

# Register your models here.
admin.site.register(Glass)
admin.site.register(Supplier)
admin.site.register(Material)
