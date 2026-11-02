from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'roll',
        'email',
        'gender',
        'department',
    )

    search_fields = ('name', 'email', 'roll')
    list_filter = ('gender', 'department')