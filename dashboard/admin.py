from django.contrib import admin

from .models import Customer, Employee, Order

admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Order)
