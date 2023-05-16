from django.contrib import admin

from apps.models import Picture


@admin.register(Picture)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id',)
    # fieldsets = (
    #     ('Image', {'fields': ('id', 'npl', 'time', 'timestamp', 'speed', 'fullimg', 'lp', 'aux', 'small', 'camera')}),
    # )


