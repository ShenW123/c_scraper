from craigslist import CraigslistHousing

### Shapefile Get Neighbourhood Metadata
import shapefile

shpf = shapefile.Reader("TorNeighbour.shp")
records = shpf.iterShapeRecords()
neighbourhoods = {}
for record in records:
    name = record.record
    bbox = record.shape.bbox
    neighbourhoods[name[1]] = [coord for coord in bbox]
### Builds a neighbourhoods dictionary with Neighbourhood Name and GPS Bounding Box

### Craigslist Scraper

cl = CraigslistHousing(site='toronto', area='tor', category='apa',
						 filters={'max_price': 2000, 'min_price': 1000})

results = cl.get_results(sort_by='newest', geotagged=True, limit=5)

def in_box(coords, box):
	if box[1] < coords[0] < box[3] and box[0] < coords[1] < box[2]:
		return True
	return False

### Compare Scraped data to see if in Neighbourhoods Metadata and keep the ones that are
myResults = []
for result in results:
	try:
		geotag = result["geotag"]
		for a, coords in neighbourhoods.items():
			if in_box(geotag, coords):
				result['area'] = a
				result['area_found'] = True
			else:
				result['area'] = "none"
				result['area_found'] = False
			myResults.append(result)
	except:
		print "No coordinates"

print myResults