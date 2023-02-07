from django.db import models

from apps.services.models import ServiceModel
from apps.users.models import UserModel


class OrderStatusModel(models.Model):
    class Meta:
        db_table = 'orders_status'

    name = models.CharField(max_length=128)


class OrderModel(models.Model):
    class Meta:
        db_table = 'orders'

    address = models.CharField(max_length=128)
    photo = models.CharField(max_length=128)
    task_description = models.TextField()
    date = models.CharField(max_length=128)
    time = models.CharField(max_length=128)
    price = models.IntegerField(default=0)
    status = models.ForeignKey(OrderStatusModel, on_delete=models.CASCADE, related_name='orders', default=1)
    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE, related_name='orders')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='orders')
    employees_count = models.IntegerField(default=1)
    employees = models.ManyToManyField(UserModel, blank=True, related_query_name='employees_orders')

