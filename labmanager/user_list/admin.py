from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('name','supervisor','user_rank','user_type','email','status','join_date' )
    list_filter = ('supervisor','user_rank','user_type','status')
    search_fields = ('description','name','supervisor','user_rank')
    # raw_id_fields = ('name',)
    date_hierarchy ='join_date'
    ordering = ('user_rank','supervisor','name')

admin.site.register(User,UserAdmin)
