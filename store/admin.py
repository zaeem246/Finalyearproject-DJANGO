from msilib.schema import RemoveIniFile
from operator import imod
from django.contrib import admin
from .models import Product, Variation, ReviewRating
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug':('product_name',)}

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    # if we dont add this class it will show the variations as Variationobject(1), 
    #but we require the proper name of variation
    list_editable = ('is_active',) 
    list_filter = ('product', 'variation_category', 'variation_value')
    

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin) 
admin.site.register(ReviewRating) 
