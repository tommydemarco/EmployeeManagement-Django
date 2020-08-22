from django.contrib import admin

from .models import Employee, Skill

# Register your models here.


#modifying the view style in the admin section
class EmployeeAdmin(admin.ModelAdmin):
    #adding what table column attributes I want to display in the list of employees
    list_display = (
        #Overrides what the __str__ magic method returns
        #(you can not add a many to many field)
        'id',
        'first_name',
        'last_name',
        'base',
        'contact_phone',
        'address',
        #adding now a column that is not related to any field, but it's generated uning a function
        'crew_code'
    )
    #function to display the column crew_code
    def crew_code(self, obj):
        return obj.first_name[0:3].upper() + obj.last_name[0:2].upper()
    #adding the possibility to make a search of the fields
    search_fields = ('first_name',)
    #adding a filter for fields that are set with a choice
    list_filter = ('base',)

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Skill)