from django.contrib import admin
from .models import Chat,Message

# Register your models here.

# zeigt was alles für den admin angezeigt wiird
class MessageAdmin(admin.ModelAdmin):    
    fields = ('text','chat','created_at', 'author', 'receiver')    
    list_display = ('created_at','chat', 'author', 'text', 'receiver')    
    search_fields = ('text',)
    
    # Register your models here

admin.site.register(Message,MessageAdmin)
admin.site.register(Chat)