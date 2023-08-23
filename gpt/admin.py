from django.contrib import admin
from .models import Code

@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    list_display = ['user', 'problem', 'language']
    list_filter = ['user', 'language']
    search_fields = ['user__username']  
