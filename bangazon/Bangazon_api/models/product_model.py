import sys
sys.path.append("../")
from django.db import models
from .product_type_model import ProductType
from .customer_model import Customer


class Product(models.Model):
    """
    Class to represent a product for sale on Bangazon
    tied to a
    particular User(customer) of bangazon API
    Extension of models.Model
    Variables:
        created: the current local date and time of creation
        name: the product's name
        
        customer: the foreign key of Customer class

    Author: Julia Kim-Chung
    """
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default="")
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField(max_length=300, default='')
    quantity = models.IntegerField()
    product_type =models.ForeignKey(ProductType, related_name="products", on_delete=models.CASCADE, blank=True, null=True)
    customer =models.ForeignKey(Customer, related_name="products", on_delete=models.CASCADE)

    def __str__(self):
        """
        Method to create a string representing a Product sold/bought by a particular User(customer)
        """

        return self.name

    class Meta:
        ordering =('name', )

