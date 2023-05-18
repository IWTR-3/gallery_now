# posts/admin.py

from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Artist)
admin.site.register(Gallery)
admin.site.register(Exhibition)
admin.site.register(Review)
admin.site.register(Theme)
