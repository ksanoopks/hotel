from django.contrib import admin
from booking.models import Hotel

# Register your models here.

class Booking(admin.ModelAdmin):
    list_display= ('name','location','rating','description','type')


admin.site.register(Hotel,Booking)


