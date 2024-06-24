from django.contrib import admin

from . import models
# Register your models here.
admin.site.register(models.Train)
# admin.site.register(models.Category)
admin.site.register(models.Comment)
class StationAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug']
admin.site.register(models.Station,StationAdmin)