import math
import geopy
import ast
import ee
from parallel_sync import wget
# Distances are measured in kilometers.
# Longitudes and latitudes are measured in degrees.
# Earth is assumed to be perfectly spherical.
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="email or host service ") #specify here
locality=input("enter the location: ")
location=geolocator.geocode(locality)
lat=location.latitude 
lon=location.longitude

earth_radius = 6271.0
degrees_to_radians = math.pi/180.0
radians_to_degrees = 180.0/math.pi

def change_in_latitude(kms):
    "Given a distance north, return the change in latitude."
    return (kms/earth_radius)*radians_to_degrees

def change_in_longitude(latitude, kms):
    "Given a latitude and a distance west, return the change in longitude."
    # Find the radius of a circle around the earth at given latitude.
    r = earth_radius*math.cos(latitude*degrees_to_radians)
    return (kms/r)*radians_to_degrees

def ten_km_square(latitude, longitude):
    slat, nlat = latitude+change_in_latitude(-3.75), latitude+change_in_latitude(3.75)
    wlon = longitude+change_in_longitude(latitude,-3.75)
    elon = longitude+change_in_longitude(latitude, 3.75)
    return(nlat, wlon, slat, elon)

def main(lon, lat):
    '''First argument degrees longitude (E is positive, W negative)
        of the landslide location,
        second argument latitude (N positive, S negative),
        in decimal format(not minutes etc.)'''
    nlat, wlon, slat, elon = ten_km_square(lat,lon)
    #print("(NLat:{:.4f},WLon:{:.4f}),(SLat:{:.4f},ELon:{:.4f});".format(nlat, wlon, slat, elon))
    region = ('[{:.4f},{:.4f}], [{:.4f},{:.4f}], [{:.4f},{:.4f}], [{:.4f},{:.4f}]'.format(wlon,nlat,elon,nlat,wlon,slat,elon,slat))
    rectangle = ('[{:.4f},{:.4f},{:.4f},{:.4f}]'.format(wlon,slat,elon,nlat))
    lister=region.split('/')
    finallist=[ast.literal_eval(i) for i in lister] # to remove apostrophe
    final = [list(value) for value in finallist] # final list
    print(final)
    import ee
    import ee.mapclient
    import ee
    ee.Initialize()
    import ee.mapclient
    start = ee.Date('2017-01-01')
    finish = ee.Date('2017-03-20')

    rectangle = ee.Geometry.Polygon(final) #passing the final value as the polygon boundaries defined 10km square area
    collection = ee.ImageCollection('COPERNICUS/S2')

    filteredCollection = collection.filterBounds(rectangle).filterDate(start,finish)

    first = filteredCollection.first()
    path = first.getDownloadURL({
  'region':final,
  'scale': 10
})
    print(path)
    urls = [path]
    wget.download('/home/path/to/save', urls[0], filenames='x.zip', extract=True) #path to your location to save a particular image
main(lon ,lat)
