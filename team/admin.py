from django.contrib import admin
from .models import Task

# class ModuleInline(admin.StackedInline):
#     model = Task


class TaskAdmin(admin.ModelAdmin):
	list_display = ['title', 'user', 'category', 'created', 'development_url', 'documentation', 'datecompleted']
   
 

admin.site.register(Task, TaskAdmin)

