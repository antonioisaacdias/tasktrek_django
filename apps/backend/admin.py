from django.contrib import admin
from .models import Project, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color','description', 'comments', 'created_at', 'updated_at', 'user', 'is_active')
    search_fields = ('name', 'color','description', 'comments')
    list_filter = ('is_active', 'created_at')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    list_per_page = 20
    readonly_fields = ('id', 'user', 'created_at', 'updated_at')
    list_select_related = ('user',)
    
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user = request.user
        super().save_model(request, obj, form, change)

    
@admin.register(Task)    
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'comments', 'created_at', 'updated_at', 'expires_at', 'is_completed', 'user', 'project')
    search_fields = ('name', 'comments')
    list_filter = ('is_completed',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    list_per_page = 20
    list_select_related = ('user', 'project')
    readonly_fields = ('id', 'user', 'created_at', 'updated_at')
    list_select_related = ('user',)
    

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user = request.user
        super().save_model(request, obj, form, change)

