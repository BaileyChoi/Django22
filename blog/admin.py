from django.contrib import admin
from .models import Post, Category

# Register your models here.
admin.site.register(Post)   # Post 모델 admin_에 등록

# slugField 자동 생성, name값으로 slug 생성
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Category,CategoryAdmin)