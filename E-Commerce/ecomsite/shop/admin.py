from django.contrib import admin
from django.db import models
from .models import Products, Order

# Register your models here.
admin.site.site_header = "E-Commerce Site"
admin.site.site_title = "Easy Shopping"
admin.site.index_title = "Manage Easy Shopping "

class Productadmin(admin.ModelAdmin):
    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")

    change_category_to_default.short_description = 'Default Category'
    list_display = ('title','category','price','discount_price')
    search_fields = ('title',)
    list_filter = ('category',)
    actions = ('change_category_to_default',)
    #fields = ('title','price',)
    list_editable = ('price','discount_price',)

class Orderadmin(admin.ModelAdmin):
    list_display = ('name','address')
    list_filter = ('city',)

admin.site.register(Products, Productadmin)
admin.site.register(Order, Orderadmin)