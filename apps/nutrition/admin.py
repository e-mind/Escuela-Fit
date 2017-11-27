from django.contrib import admin

from .models import Nutrition, Nutrition_Food


class NutritionAdmin(admin.ModelAdmin):
	list_display = ['pk', 'student', 'schedule', 'create_date']

class Nutrition_FoodAdmin(admin.ModelAdmin):
	list_display = ['nutrition', 'food_id', 'food_table']


admin.site.register(Nutrition, NutritionAdmin)
admin.site.register(Nutrition_Food, Nutrition_FoodAdmin)
