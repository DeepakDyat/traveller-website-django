from django.contrib import admin

# Register your models here.
from .models import contact,package,booking,checkout
admin.site.register(contact)
admin.site.register(package)
admin.site.register(booking)
admin.site.register(checkout)