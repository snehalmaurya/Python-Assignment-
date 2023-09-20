from django.contrib import admin
from .models import user, complaint, policeStation,emergency
# Register your models here.

admin.site.site_header = "E-police admin"
admin.site.index_title = "Admin dashboard"
admin.site.site_title = "E-police station"

admin.site.register(user)
admin.site.register(complaint)
admin.site.register(policeStation)
admin.site.register(emergency)