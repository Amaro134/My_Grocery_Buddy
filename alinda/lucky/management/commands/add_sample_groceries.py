from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from lucky.models import Task, CATEGORY_CHOICES

class Command(BaseCommand):
    help = 'Adds sample grocery items for a user'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username to add sample groceries for')

    def handle(self, *args, **options):
        username = options['username']
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'User "{username}" does not exist. Please create the user first.'))
            return

        sample_groceries = [
            {'title': 'Milk', 'quantity': 2, 'category': 'Dairy', 'price': 4.99},
            {'title': 'Bread', 'quantity': 1, 'category': 'Bakery', 'price': 3.49},
            {'title': 'Eggs', 'quantity': 1, 'category': 'Dairy', 'price': 5.99},
            {'title': 'Bananas', 'quantity': 6, 'category': 'Produce', 'price': 2.99},
            {'title': 'Chicken Breast', 'quantity': 1, 'category': 'Meat', 'price': 8.99},
            {'title': 'Rice', 'quantity': 1, 'category': 'Pantry', 'price': 4.49},
            {'title': 'Orange Juice', 'quantity': 1, 'category': 'Beverages', 'price': 3.99},
            {'title': 'Potatoes', 'quantity': 5, 'category': 'Produce', 'price': 3.49},
            {'title': 'Cheese', 'quantity': 1, 'category': 'Dairy', 'price': 5.99},
            {'title': 'Tomatoes', 'quantity': 4, 'category': 'Produce', 'price': 2.49},
            {'title': 'Pasta', 'quantity': 2, 'category': 'Pantry', 'price': 2.99},
            {'title': 'Ice Cream', 'quantity': 1, 'category': 'Frozen', 'price': 6.99},
            {'title': 'Chips', 'quantity': 2, 'category': 'Snacks', 'price': 3.99},
            {'title': 'Yogurt', 'quantity': 4, 'category': 'Dairy', 'price': 5.49},
            {'title': 'Apples', 'quantity': 6, 'category': 'Produce', 'price': 4.99},
        ]

        created_count = 0
        for item_data in sample_groceries:
            task, created = Task.objects.get_or_create(
                user=user,
                title=item_data['title'],
                defaults={
                    'quantity': item_data['quantity'],
                    'category': item_data['category'],
                    'price': item_data['price'],
                    'complete': False,
                    'status': 'active'
                }
            )
            if created:
                created_count += 1

        self.stdout.write(self.style.SUCCESS(
            f'Successfully added {created_count} sample grocery items for user "{username}"!'
        ))

