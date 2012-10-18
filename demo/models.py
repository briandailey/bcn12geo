from django.contrib.gis.db import models

# Create your models here.
class Blockgroup(models.Model):
    statefp = models.CharField(max_length=2)
    countyfp = models.CharField(max_length=3)
    tractce = models.CharField(max_length=6)
    blkgrpce = models.CharField(max_length=1)
    geoid = models.CharField(max_length=12)
    namelsad = models.CharField(max_length=13)
    mtfcc = models.CharField(max_length=5)
    funcstat = models.CharField(max_length=1)
    aland = models.FloatField()
    awater = models.FloatField()
    intptlat = models.CharField(max_length=11)
    intptlon = models.CharField(max_length=12)

    geom = models.PolygonField(srid=4269)

    objects = models.GeoManager()

# Auto-generated `LayerMapping` dictionary for Blockgroup model
blockgroup_mapping = {
    'statefp' : 'STATEFP',
    'countyfp' : 'COUNTYFP',
    'tractce' : 'TRACTCE',
    'blkgrpce' : 'BLKGRPCE',
    'geoid' : 'GEOID',
    'namelsad' : 'NAMELSAD',
    'mtfcc' : 'MTFCC',
    'funcstat' : 'FUNCSTAT',
    'aland' : 'ALAND',
    'awater' : 'AWATER',
    'intptlat' : 'INTPTLAT',
    'intptlon' : 'INTPTLON',
    'geom' : 'POLYGON',
}

class Crime(models.Model):
    type = models.CharField(max_length=32)
    case_no = models.CharField(max_length=32)
    address = models.CharField(max_length=64)
    date = models.DateTimeField(null=True)

    pt = models.PointField(null=True)

    objects = models.GeoManager()

class Block(models.Model):
    statefp = models.CharField(max_length=2)
    countyfp = models.CharField(max_length=3)
    statefp10 = models.CharField(max_length=2)
    countyfp10 = models.CharField(max_length=3)
    tractce10 = models.CharField(max_length=6)
    blockce10 = models.CharField(max_length=4)
    suffix1ce = models.CharField(max_length=1)
    geoid = models.CharField(max_length=16)
    name = models.CharField(max_length=11)
    mtfcc = models.CharField(max_length=5)
    ur10 = models.CharField(max_length=1)
    uace10 = models.CharField(max_length=5)
    funcstat = models.CharField(max_length=1)
    aland = models.FloatField()
    awater = models.FloatField()
    intptlat = models.CharField(max_length=11)
    intptlon = models.CharField(max_length=12)
    geom = models.PolygonField(srid=4269)
    objects = models.GeoManager()

# Auto-generated `LayerMapping` dictionary for Block model
block_mapping = {
    'statefp' : 'STATEFP',
    'countyfp' : 'COUNTYFP',
    'statefp10' : 'STATEFP10',
    'countyfp10' : 'COUNTYFP10',
    'tractce10' : 'TRACTCE10',
    'blockce10' : 'BLOCKCE10',
    'suffix1ce' : 'SUFFIX1CE',
    'geoid' : 'GEOID',
    'name' : 'NAME',
    'mtfcc' : 'MTFCC',
    'ur10' : 'UR10',
    'uace10' : 'UACE10',
    'funcstat' : 'FUNCSTAT',
    'aland' : 'ALAND',
    'awater' : 'AWATER',
    'intptlat' : 'INTPTLAT',
    'intptlon' : 'INTPTLON',
    'geom' : 'POLYGON',
}

class County(models.Model):
    statefp10 = models.CharField(max_length=2)
    countyfp10 = models.CharField(max_length=3)
    countyns10 = models.CharField(max_length=8)
    geoid10 = models.CharField(max_length=5)
    name10 = models.CharField(max_length=100)
    namelsad10 = models.CharField(max_length=100)
    lsad10 = models.CharField(max_length=2)
    classfp10 = models.CharField(max_length=2)
    mtfcc10 = models.CharField(max_length=5)
    csafp10 = models.CharField(max_length=3)
    cbsafp10 = models.CharField(max_length=5)
    metdivfp10 = models.CharField(max_length=5)
    funcstat10 = models.CharField(max_length=1)
    aland10 = models.FloatField()
    awater10 = models.FloatField()
    intptlat10 = models.CharField(max_length=11)
    intptlon10 = models.CharField(max_length=12)
    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager()

# Auto-generated `LayerMapping` dictionary for County model
county_mapping = {
    'statefp10' : 'STATEFP10',
    'countyfp10' : 'COUNTYFP10',
    'countyns10' : 'COUNTYNS10',
    'geoid10' : 'GEOID10',
    'name10' : 'NAME10',
    'namelsad10' : 'NAMELSAD10',
    'lsad10' : 'LSAD10',
    'classfp10' : 'CLASSFP10',
    'mtfcc10' : 'MTFCC10',
    'csafp10' : 'CSAFP10',
    'cbsafp10' : 'CBSAFP10',
    'metdivfp10' : 'METDIVFP10',
    'funcstat10' : 'FUNCSTAT10',
    'aland10' : 'ALAND10',
    'awater10' : 'AWATER10',
    'intptlat10' : 'INTPTLAT10',
    'intptlon10' : 'INTPTLON10',
    'geom' : 'POLYGON',
}
