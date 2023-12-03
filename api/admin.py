from django.contrib import admin
from .models import Note
# Register your models here.


class NoteAdmin(admin.ModelAdmin):
    list_display = ['note', 'created', 'updated']
    list_filter = ['note']
    search_fields = ['note']


admin.site.register(Note, NoteAdmin)
