from django.db import models

from markets.models import Location, Product


class Customer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def orders_info(self):
        orders = Order.objects.filter(customer=self)
        total_cost = sum([order.product.price for order in orders])
        return {'orders': orders, 'total_cost': total_cost}

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def orders_info(self):
        orders = Order.objects.filter(employee=self)
        total_cost = sum([order.product.price for order in orders])
        return {'orders': orders, 'total_cost': total_cost}

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()

