from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Customer, Employee, Order


class CustomerListView(ListView):
    model = Customer
    template_name = 'dashboard/customer_list.html'
    context_object_name = 'customers'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'dashboard/customer_detail.html'
    context_object_name = 'customer'

    def customer_detail(request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        orders = Order.objects.filter(customer=customer)
        total_price = sum([order.product.price for order in orders])
        return render(request, 'dashboard/customer_detail.html', {
        'customer': customer,
        'orders': orders,
        'total_price': total_price,
    })

class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'dashboard/customer_form.html'
    fields = '__all__'

class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'dashboard/customer_form.html'
    fields = '__all__'

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'dashboard/customer_confirm_delete.html'
    success_url = reverse_lazy('customer_list')

class EmployeeListView(ListView):
    model = Employee
    template_name = 'dashboard/employee_list.html'
    context_object_name = 'employees'

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'dashboard/employee_detail.html'
    context_object_name = 'employee'

    def employee_detail(request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        orders = Order.objects.filter(employee=employee)
        total_price = sum([order.product.price for order in orders])
        return render(request, 'dashboard/employee_detail.html', {
        'employee': employee,
        'orders': orders,
        'total_price': total_price,
    })

class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'dashboard/employee_form.html'
    fields = '__all__'

class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'dashboard/employee_form.html'
    fields = '__all__'

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'dashboard/employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')

class OrderListView(ListView):
    model = Order
    template_name = 'dashboard/order_list.html'
    context_object_name = 'orders'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'dashboard/order_detail.html'
    context_object_name = 'orders'

    def order_detail(request, pk):
        order = get_object_or_404(Order, pk=pk)
        return render(request, 'dashboard/order_detail.html', {
        'order': order,
    })

class OrderCreateView(CreateView):
    model = Order
    template_name = 'dashboard/order_form.html'
    fields = '__all__'

class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'dashboard/order_form.html'
    fields = '__all__'

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'dashboard/order_confirm_delete.html'
    success_url = reverse_lazy('order_list')

