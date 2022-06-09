from django.contrib import admin

from manager.models import Storage
from .models import User, Company, Employee, Manager, Accountant

from django.contrib.auth.admin import UserAdmin

from . import forms
from . import models

admin.site.register(User)
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Manager)
admin.site.register(Accountant)
admin.site.register(Storage)


# Define the admin class
#class ManagerAdmin(admin.ModelAdmin):
 #   list_display = ['first_name', 'last_name', 'email', 'username', 'passport_numer', 'passport_series', 'age', 'company']

# Register the admin class with the associated model
#admin.site.register(Manager, ManagerAdmin)

# Register the Admin classes for Book using the decorator
# Define the admin class
#class AccountantAdmin(admin.ModelAdmin):
 #   list_display = ['first_name', 'last_name', 'email', 'username', 'passport_numer', 'passport_series', 'age', 'company']

# Register the admin class with the associated model
#admin.site.register(Accountant, AccountantAdmin)

#@admin.register(Company)
#class BookAdmin(admin.ModelAdmin):
#    pass
#@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = forms.CustomUserCreationForm
    form = forms.CustomUserChangeForm
    list_display = ['first_name', 'last_name', 'email', 'username', 'passport_numer', 'passport_series', 'age']
    model = models.User
# Register the Admin classes for BookInstance using the decorator
