import sys
sys.path.append("../")
from django.test import TestCase
from django.contrib.auth.models import User
from bangazon_ui.models.customer_model import Customer
from bangazon_ui.models.payment_type_model import PaymentType
from bangazon_ui.models.product_model import Product
from bangazon_ui.models.product_type_model import ProductType
from bangazon_ui.models.order_model import Order


class TestOrderModel(TestCase):

    """
    This is a test to build implementation code for the Order Model.
    Author: Shawn Mitchell
    """

    def test_order_has_required_fields(self):

        user = User.objects.create_user(
        first_name="Dani",
        last_name="Dani",
        username="danidani",
        password="asdf1234"
        )

        customer = Customer.objects.create(
        user=user,
        address="3040 NSS Drive",
        city="Nashville",
        state="TN",
        zip_code="12345",
        phone="123456789"
        )

        payment = PaymentType.objects.create(
        customer=customer,
        payment_type="Visa",
        account_number="12345678",
        ccv="111",
        expiration_date="2017-01-01"
        )

        product_type = ProductType.objects.create(
        label= 'musical instruments'
        )

        product = Product.objects.create(
        customer = customer,
        name = 'cello',
        price = '100',
        description = 'yoyo-ma',
        product_type = product_type,
        quantity = 5
        )

        order = Order.objects.create(
        customer=customer,
        payment_type= payment,
        )
        # The  .add() allows the user to add a product to the order table and .save() allows the user to save the product

        order.product.add(product)
        order.save()

        # Check to see if there  is an object instance of Customer / PaymentType/ Product
        self.assertIsInstance(order.customer, Customer)
        self.assertIsInstance(order.payment_type, PaymentType)
        #QuerysetEqual is an assertion native to Django and used to test the .all() or products returned after the .save() has been invoked.
        self.assertQuerysetEqual(order.product.all(), ['<Product: cello>'])
