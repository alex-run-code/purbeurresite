from django.contrib import admin
from .models import Food, Food_category, Category



class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'nutriscore')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class Food_categoryAdmin(admin.ModelAdmin):
    list_display = ('food_id', 'category_id')


admin.site.register(Food, FoodAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Food_category, Food_categoryAdmin)




