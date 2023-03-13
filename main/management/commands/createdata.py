from django.core.management.base import BaseCommand
from faker import Faker, providers
from main.models import Category, Product
import random

CATEGORIES = [
    'Technology',
    'Marine',
    'Boat',
    'Outboard',
    'GPS'
]

class Provider(providers.BaseProvider):
    
    def my_category(self):
        return self.random_element(CATEGORIES)
    

class Command(BaseCommand):
    help = "Command Information"

    def handle(self, *args, **kwargs):

        fake = Faker()
        fake.add_provider(Provider)
        
        for _ in range(5):
          cat = fake.unique.my_category()
          Category.objects.create(
              name = cat
          )

        for _ in range(20):
            name = fake.text(max_nb_chars=30)
            cat_id = random.randint(1,5)
            description = fake.text(max_nb_chars=200)
            price = round(random.uniform(900.99, 10000.99),2)

            Product.objects.create(
                name = name,
                description = description,
                price = price,
                category_id=cat_id,
                image ="product-images/default.jpg"
            )

        products_count = Product.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Number of products inserted: {products_count}"))

