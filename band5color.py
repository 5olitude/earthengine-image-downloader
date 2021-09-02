# This is the updated code how we can download the colorful stellite images of Band5

import ee
ee.Authenticate()
ee.Initialize()

def maskS2clouds(image):
    qa = image.select('QA60')

    cloudBitMask = 1 << 10
    cirrusBitMask = 1 << 11

    mask = qa.bitwiseAnd(cloudBitMask).eq(0)
    mask = mask.bitwiseAnd(cirrusBitMask).eq(0)

    return image.updateMask(mask).divide(10000)


# location Cordinates
geom = ee.Geometry.Polygon([[24.8769,60.2263], [25.0148,60.2263], [24.8769,60.1578], [25.0148,60.1578]])  

#Defining The bands and the date range so that you can filter the images in the specific date
collection = (ee.ImageCollection("COPERNICUS/S2")
             
              .select(['B4', 'B3', 'B2', 'QA60'])
             
              .filter(ee.Filter.date('2019-01-01', '2019-03-31'))
             
              .filterBounds(geom)
             
              .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))
             
              .map(maskS2clouds)
             )


image = collection.sort('system:index', opt_ascending=False).mosaic()



image = image.visualize(bands=['B4', 'B3', 'B2'],
                        min=[0.0, 0.0, 0.0],
                        max=[0.3, 0.3, 0.3]
                       )

.
task_config = {
    'region': geom.coordinates().getInfo(),
    'scale': 10,
    'crs': 'EPSG:4326',
    'description': 'mysat'
}

# Exporting Images to our google drive usually the images are of type tiff format upto 10mb per file

task = ee.batch.Export.image.toDrive(image, **task_config)
task.start()
