from django.core.management.base import BaseCommand

from catalog.models import Category, Product

from django.core.management import call_command


class Command(BaseCommand):
    help = 'Add products to database'


    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category, _ = Category.objects.get_or_create(name='Техника', description='Бытовая техника')

        products = [
            {'name': 'Кондиционер', 'description': 'Чтобы было холоднее', 'category': category, 'price': '25000'},
            {'name': 'Насос', 'description': 'Мощный и дешевый', 'category': category, 'price': '5000'},

        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists {product.name}'))