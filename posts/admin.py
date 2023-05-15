# posts/admin.py

from django.contrib import admin
from .models import Artist, Gallery, Exhibition, Review, Theme


class CustomAdmin(admin.ModelAdmin):
    list_display = ['tag_list']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


# Register your models here.
admin.site.register(Artist)
admin.site.register(Gallery)
admin.site.register(Exhibition, CustomAdmin)
admin.site.register(Review)
admin.site.register(Theme)
