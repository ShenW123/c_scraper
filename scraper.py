import settings
import utils
import time

## Craigslist Scraper

# Don't hammer their servers, next time grab the data and then use that instead for Testing
from craigslist import CraigslistHousing

def scrape_area(areas):

	cl = CraigslistHousing(site=settings.CRAIGSLIST_SITE, area=areas, category=settings.CRAIGSLIST_HOUSING_SECTION, filters={'max_price': settings.MAX_PRICE, 'min_price': settings.MIN_PRICE})

	results = cl.get_results(sort_by='newest', geotagged=True, limit=5)

	neighbourhoods = utils.getNeighbourhoods()

	## Compare Scraped data to see if in Neighbourhoods Metadata and keep the ones that are
	myResults = []
	for result in results:
		try:
			geotag = result["geotag"]
			result['area'] = "none"
			result['area_found'] = False
			for a, coords in neighbourhoods.items():
				if utils.in_box(geotag, coords):
					result['area'] = a
					result['area_found'] = True
					break
			myResults.append(result)
		except:
			pass

	return myResults

def doScrape():
	all_results = []
	for area in settings.AREAS:
		all_results += scrape_area(area)
	print("{}: Got {} results".format(time.ctime(), len(all_results)))
	return all_results

