from django.core.management.base import BaseCommand
from shop.models import Category, Product


class Command(BaseCommand):
    help = 'Fill database with sample data'

    def handle(self, *args, **options):
        # Clear existing data
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Create categories
        category1 = Category.objects.create(name='мучные изделия')

        self.stdout.write(self.style.SUCCESS('Data successfully filled.'))
