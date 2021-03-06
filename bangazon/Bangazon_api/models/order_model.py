import sys
sys.path.append("../")
from django.db import models
from django.contrib.auth.models import User
from Bangazon_api.models.customer_model import Customer
from Bangazon_api.models.payment_type_model import PaymentType
from Bangazon_api.models.product_model import Product


class Order (models.Model):
    """
    The Order table pulls information from PaymentType and Product via a join 
    """

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    completed = models.IntegerField(default = 0)
    payment_type = models.ForeignKey(PaymentType, null=True, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, through='OrderProduct')

    # This will allow the Order class to be recgonized in Django also as Orders
    class Meta:
        verbose_name_plural = "Orders"
    # Returning the object to show whether the order has been completed or not (0 off 1 on)

    def __str__(self):
        return '{}'.format(self.completed)


class OrderProduct(models.Model):
    """
    """
    product = models.ForeignKey(Product, null=True)
    order = models.ForeignKey(Order, null=True)