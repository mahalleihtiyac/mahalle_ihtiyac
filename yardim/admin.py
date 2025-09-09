
from django.contrib import admin
from .models import HelpRequest, Category, Profile, Comment, Message  # tüm modelleri import ettik

# Admin paneli başlıklarını özelleştir
admin.site.site_header = "Mahalle Yardım Yönetim Sistemi"
admin.site.site_title = "Mahalle Yardım Yönetim Sistemi"
admin.site.index_title = "Yönetim Paneli"

@admin.register(HelpRequest)
class HelpRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'help_date', 'is_urgent')  # listelenecek alanlar
    list_filter = ('user', 'created_at', 'help_date', 'is_urgent')  # filtreleme yapılacak alanlar
    search_fields = ('title', 'description')  # arama yapılacak alanlar
    date_hierarchy = 'created_at'  # tarihe göre hiyerarşi
    ordering = ('-created_at',)  # sıralama

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'location', 'phone_number')
    list_filter = ('role', 'location')
    search_fields = ('user__username', 'bio', 'location')
    readonly_fields = ('user',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'help_request', 'created_at')
    list_filter = ('created_at', 'help_request')
    search_fields = ('content', 'user__username')
    readonly_fields = ('created_at',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'created_at', 'is_read')
    list_filter = ('created_at', 'is_read')
    search_fields = ('content', 'sender__username', 'receiver__username')
    readonly_fields = ('created_at',)