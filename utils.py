import settings
import shapefile
import json
from slackclient import SlackClient

def in_box(geotag, coords):
	if coords[1] < geotag[0] < coords[3] and coords[0] < geotag[1] < coords[2]:
		return True
	return False

def getNeighbourhoods():
	try:
		with open(settings.NEIGHBOURHOOD_File) as data_file:
			neighbourhoods = json.load(data_file)
	except:
		neighbourhoods = makeNeighbourhoods()
	return neighbourhoods

def makeNeighbourhoods():
	### Shapefile Get Neighbourhood Metadata
	shpf = shapefile.Reader(settings.NEIGHBOURHOOD_MAP)
	records = shpf.iterShapeRecords()
	neighbourhoods = {}
	for record in records:
		name = record.record
		bbox = record.shape.bbox
		neighbourhoods[name[1]] = [coord for coord in bbox]

	with open(settings.NEIGHBOURHOOD_File, 'w') as outfile:
		json.dump(neighbourhoods, outfile)

	return neighbourhoods

def notifySlack(myResults):
	sc = SlackClient(settings.SLACK_TOKEN)
	for posting in myResults:
		desc = "{0} | {1} | {2} | <{3}> | Transit <Work {4}> <DT {5}>".format(posting["area"], posting["price"], posting["name"], posting["url"], posting["locations"]["work"], posting["locations"]["dt"])
		sc.api_call(
			"chat.postMessage", channel=settings.SLACK_CHANNEL, text=desc
		)