from django.contrib import admin
from .models import *


class ModelAdminMixin:
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Only set added_by during the first save.
            obj.updated_by = request.user
        super().save_model(request, obj, form, change)


class ProductAdmin(ModelAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'title_ar', 'title_en', 'country', 'city', 'price')
    list_display_links = ('title_ar', 'title_en')
    list_filter = ('country','city',)


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_ar', 'name_en', 'display')
    list_editable = ['display']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_ar', 'name_en', 'show')
    list_editable = ['name_ar', 'name_en', 'show']


admin.site.register(Product, ProductAdmin)
admin.site.register(Profile)
admin.site.register(ProductImage)
admin.site.register(Category, CategoryAdmin )
admin.site.register(Country, CountryAdmin)