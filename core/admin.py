from django.contrib import admin

from core.models import ActivityLog, Todo, Pai


class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('type', 'logged_user', 'created_at')


class TodoAdmin(admin.ModelAdmin):
    list_display = ('description', 'done')


class PaiAdmin(admin.ModelAdmin):
    list_display = ('name', 'countfilhos')


admin.site.register(ActivityLog, ActivityLogAdmin)
admin.site.register(Todo, TodoAdmin)
admin.site.register(Pai, PaiAdmin)
