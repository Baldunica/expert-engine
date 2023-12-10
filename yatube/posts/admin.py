from django.contrib import admin

# Register your models here.
from .models import Post,Group

class PostAdmin(admin.ModelAdmin):
  list_display = ('pk','author','pub_date','text','group')
  search_fields = ('text',)
  list_filter = ('pub_date',)
  list_editable = ('group',)
  empty_value_display = '-null-' 

admin.site.register(Post,PostAdmin)
admin.site.register(Group)