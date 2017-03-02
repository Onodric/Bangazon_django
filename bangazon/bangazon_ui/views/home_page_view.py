from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bangazon_ui.models import *
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate

class HomePageView(TemplateView):

    template_name = 'bangazon_ui/home_page.html'

    def context_data(request):
        """

        """
        context = {}
        product_type_list_home = product_type_model.ProductType.objects.all()[:10]
        for product_type in product_type_list_home:
            product_list_home = product_model.Product.objects.filter(product_type = product_type.pk).order_by("-created")
            context.update({product_type: product_list_home})
        return render(request, 'bangazon_ui/product_type_list.html', {"context": context})


