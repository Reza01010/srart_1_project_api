from django.contrib import admin

from .models import Item, Jonyur, JonyurUser
# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'name')


admin.site.register(Item, ItemAdmin)


class JonyurUserAdmin(admin.ModelAdmin):
    list_display = ('age', 'last_name', 'first_name')


admin.site.register(JonyurUser, JonyurUserAdmin)


class JonyurAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', )


admin.site.register(Jonyur, JonyurAdmin)
