from django.contrib import admin
from chat.models import Message


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'timestamp', 'answered', 'closed', 'freeze')


admin.site.register(Message, CategoryAdmin)

