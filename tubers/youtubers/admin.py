from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html

# Register your models here.


class YtAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    list_display = ('id', 'myphoto', 'name', 'category', 'price', 'subs_count', 'is_featured')
    list_display_links = ('name',)
    search_fields = ('name', 'category')
    list_filter = ('category', 'camera_type')
    list_editable = ('is_featured',)


admin.site.register(Youtuber, YtAdmin)
