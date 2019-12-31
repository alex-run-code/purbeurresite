from django.core.management.base import BaseCommand, CommandError
from fooddb import dbfiller

class Command(BaseCommand):
    help = 'fills the database'

    def handle(self, *args, **options):
        dbfiller.add_food_in_db()
        dbfiller.fc_list_filler()
        dbfiller.add_categories_in_db()
        dbfiller.fills_fc_database()
        self.stdout.write(self.style.SUCCESS('Database filled'))
