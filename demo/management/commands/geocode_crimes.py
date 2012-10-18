import time, datetime

from geopy import geocoders
from geopy.geocoders.base import GeocoderError
from geopy.geocoders.google import GTooManyQueriesError, GQueryError

from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point

from demo.models import Crime

class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        g = geocoders.Google()

        for crime in Crime.objects.filter(pt__isnull=True).values('address').distinct():
            print "Sleeping..."
            time.sleep(2)
            full_address = "{address} {city}, {state}".format(
                    address=crime['address'],
                    city='Nashville',
                    state='TN')
            print "Geocoding %s" % full_address

            try:
                for place, (lat, lng) in g.geocode(full_address, exactly_one=False):
                    Crime.objects.filter(address=crime['address']).update(pt=Point(lng, lat))

                    # crime.pt = Point(lng, lat)
                    # crime.save()
            except GTooManyQueriesError:
                print GTooManyQueriesError
                exit('Error occurred that prevents further execution. (GTooManyQueriesError)')
            except GQueryError:
                # Couldn't geocode due to address issues.
                print "Failed to encode %s" % crime.address
            except GeocoderError:
                exit('Unknown error occurred that prevents further execution.')
                self.stdout.write("%s" % datetime.datetime.now())
                self.stdout.write(GeocoderError)

        self.stdout.write("%s: Successfully processed remaining records.\n" % datetime.datetime.now())
