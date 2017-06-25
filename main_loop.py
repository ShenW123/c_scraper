import settings
import time
import sys
import traceback
import utils
from scraper import doScrape
from dbchecker import addResultsDB
from clearTestDB import clearTable
from transitlocations import locationService


if __name__ == "__main__":

	myResults = [{'area_found': True, 'price': u'$1700', 'datetime': u'2017-05-20 16:12', 'has_map': True, 'id': u'6140474228', 'name': u'Apt close to Uoft avail July 1st (incl Utilities)', 'area': 'Kensington-Chinatown (78)', 'url': u'http://toronto.craigslist.org/tor/apa/6140474228.html', 'geotag': (43.656893, -79.399849), 'has_image': False, 'where': u'Spadina/College'}, 
	{'area_found': True, 'price': u'$1899', 'datetime': u'2017-05-20 15:59', 'has_map': True, 'id': u'6134095162', 'name': u'Looking for Comport & Luxury? This Furnished Condo is perfect for you!', 'area': 'Islington-City Centre West (14)', 'url': u'http://toronto.craigslist.org/tor/apa/6134095162.html', 'geotag': (43.63738, -79.53651), 'has_image': True, 'where': u'Bloor/Kipling'}, 
	{'area_found': True, 'price': u'$1799', 'datetime': u'2017-05-20 15:57', 'has_map': True, 'id': u'6131118123', 'name': u'FULLY FURNISHED Large Studio Condo with Phone, Internet, TV & Cable', 'area': 'Waterfront Communities-The Island (77)', 'url': u'http://toronto.craigslist.org/tor/apa/6131118123.html', 'geotag': (43.654382, -79.37901), 'has_image': True, 'where': u'Yonge/Dundas'}, 
	{'area_found': True, 'price': u'$1645', 'datetime': u'2017-05-20 15:46', 'has_map': True, 'id': u'6130901968', 'name': u'Avail. now Must see  1 bedroom Toronto Yonge Eglinton Apartments - Or', 'area': 'Mount Pleasant East (99)', 'url': u'http://toronto.craigslist.org/tor/apa/6130901968.html', 'geotag': (43.708146, -79.399009), 'has_image': True, 'where': u'Toronto'}]
	
	while True:
		print("{}: Starting scrape cycle".format(time.ctime()))
		try:
			# myResults = doScrape() # TEST: Comment out during testing
			uniqueResults = addResultsDB(myResults)
			for result in uniqueResults:
				result['locations'] = locationService(result['geotag'])
			utils.notifySlack(uniqueResults)
			clearTable() # TEST: Uncomment during testing
		except KeyboardInterrupt:
			print("Exiting....")
			sys.exit(1)
		except Exception as exc:
			print("Error with the scraping:", sys.exc_info()[0])
			traceback.print_exc()
		else:
			print("{}: Successfully finished scraping".format(time.ctime()))
		time.sleep(settings.SLEEP_INTERVAL)