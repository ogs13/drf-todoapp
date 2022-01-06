from django.contrib import admin

# Register your models here.
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'date',
        'done'
    ) 
    list_display_links = (
        'id',
        'title'
    )
    search_fields = (
        'id',
        'title',
        'description'
    )
    #list_editable = ()
    list_filter = (
        'date',
        'done'
    )

admin.site.register(Todo, TodoAdmin)