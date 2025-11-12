from .models import Product, Category

class ProductListInCategory:

    @staticmethod
    def product_list(category_id):
        products = Product.objects.filter(category_id=category_id)

        return products