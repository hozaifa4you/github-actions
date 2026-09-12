from django.contrib import admin

from .models import Home


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at")
    search_fields = ("title", "description")
