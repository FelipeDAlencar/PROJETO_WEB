from django.contrib import admin
from .models import Hotel, Comentario

class HotelAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('nome',)}

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Comentario)
