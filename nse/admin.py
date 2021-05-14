from django.contrib import admin
from .models import nifty,banknifty,Customer,members

admin.site.register(nifty)
admin.site.register(banknifty)
admin.site.register(Customer)

@admin.register(members)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','password')
