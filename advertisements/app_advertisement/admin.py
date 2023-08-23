from django.contrib import admin
from .models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    
    list_display = ['id', 'title', 'description', 'price', 
    'created_date', 'updated_date', 'action']


    list_filter = ['action', 'created_at']

    actions = ['make_action_as_false', 'make_action_as_true']

    fieldsets = (
        (
            'Общее', {
                'fields': ('title', 'description')
                }
        ),

        (
            'Финансы', {
                'fields': ('price', 'action'),
                'classes': ['collapse']
                }
        ),
    )
    

    #у выделенных объектов заменяет значения поля торг на нет
    @admin.action(description="Убрать возможность торга")
    def make_action_as_false(self, request, queryset):
        queryset.update(action=False)

    @admin.action(description="Добавить возможность торга")
    def make_action_as_true(self, request, queryset):
        queryset.update(action=True)




admin.site.register(Advertisement, AdvertisementAdmin)


