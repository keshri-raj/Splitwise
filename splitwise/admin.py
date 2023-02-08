from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Group)
admin.site.register(User)
admin.site.register(Activity)
admin.site.register(Split)

