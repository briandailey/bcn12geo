# Create your views here.
from demo.models import Crime
from django.contrib.gis.geos import Polygon
from django.http import HttpResponse
import json

def crime_dots(request):
    coords = request.GET['bbox'].split(',')
    bbox = Polygon.from_bbox(coords)

    crimes = Crime.objects.filter(pt__within=bbox)

    geojson_dict = {
        "type": "FeatureCollection",
        "features": [crime_to_geojson(crime) for crime in crimes ]
    }

    return HttpResponse(json.dumps(geojson_dict), content_type='application/json')

def crime_to_geojson(crime):
    """ This could also be done with TileStache.Goodies.Providers.PostGeoJSON """
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [crime.pt.x, crime.pt.y]
        },
        "properties": {
            "description": """
                <strong>{type}</strong>
                <br/>
                {address}
                <br/>
                """.format(
                    type=crime.type,
                    address=crime.address,
                )
        },
        "id": crime.id,
    }
