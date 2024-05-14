from django.contrib import admin
from .models import CarMake, CarModel

# Define CarModelInline class
class CarModelInline(admin.TabularInline):
    model = CarModel

# Define CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    # Define any customizations for CarModel admin here
    pass

# Define CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    # Define any customizations for CarMake admin here
    pass

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)