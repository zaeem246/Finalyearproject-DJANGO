from msilib.schema import RemoveIniFile
from operator import imod
from django.contrib import admin
from .models import Product, Variation, ReviewRating, ProductGallery
import admin_thumbnails
# Register your models here.
@admin_thumbnails.thumbnail('image') 
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug':('product_name',)}
    inlines = [ProductGalleryInline]


class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    # if we dont add this class it will show the variations as Variationobject(1), 
    #but we require the proper name of variation
    list_editable = ('is_active',) 
    list_filter = ('product', 'variation_category', 'variation_value')
    

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin) 
class ReviewRatingAdmin(admin.ModelAdmin):
    list_display = ('product', 'subject', 'rating', 'status', 'created_at')
    list_filter = ('product', 'status')
    search_fields = ('subject', 'review')
admin.site.register(ReviewRating, ReviewRatingAdmin)
admin.site.register(ProductGallery)


