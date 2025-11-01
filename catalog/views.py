from django.shortcuts import render
from django.http import HttpResponse

from catalog.models import Product
from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


# def home(request):
#     products = Product.objects.all()
#     context = {
#         'products': products
#     }
#     return render(request, 'catalog/home.html', context=context)


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return HttpResponse(f'{name}, спасибо за сообщение')

# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         return HttpResponse(f'{name}, спасибо за сообщение')
#     return render(request, 'catalog/contacts.html')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


# def product_detail(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     context = {
#         'product': product,
#     }
#     return render(request, 'catalog/product_detail.html', context=context)






