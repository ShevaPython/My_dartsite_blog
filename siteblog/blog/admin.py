from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import Post, Category, Tag


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('title', 'id', 'created_at', 'is_publish', 'get_photo', 'view',)
    list_display_links = ('id','title')
    search_fields = ('id','title')
    list_filter = ('category',)
    form = PostAdminForm
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ('view','created_at','get_photo',)


    def get_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src={object.photo.url} width=50 >')
        return F'___'

    get_photo.short_description = 'Фото'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
