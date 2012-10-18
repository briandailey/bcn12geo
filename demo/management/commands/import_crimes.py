import csv
from optparse import make_option
from demo.models import Crime
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = ''

    option_list = BaseCommand.option_list + (
            make_option('--path',
                action='store',
                dest='path',
                default='',
                help='Path to crime CSV file.'),
            )

    def handle(self, *args, **options):
        path = options.get('path')

        with open(path) as csv_file:
            csvreader = csv.DictReader(csv_file)
            for row in csvreader:
                Crime.objects.create(
                        type=row['Type'],
                        case_no=row['Case Number'],
                        address=row['Location'],
                    )


