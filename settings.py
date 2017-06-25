import json

## Price

# The minimum rent you want to pay per month.
MIN_PRICE = 1000

# The maximum rent you want to pay per month.
MAX_PRICE = 2000

## Location preferences

# The Craigslist site you want to search on.
# For instance, https://sfbay.craigslist.org is SF and the Bay Area.
# You only need the beginning of the URL.
CRAIGSLIST_SITE = 'toronto'

# What Craigslist subdirectories to search on.
# For instance, https://sfbay.craigslist.org/eby/ is the East Bay, and https://sfbay.craigslist.org/sfc/ is San Francisco.
# You only need the last three letters of the URLs.
AREAS = ["tor"]

## Search type preferences

# The Craigslist section underneath housing that you want to search in.
# For instance, https://sfbay.craigslist.org/search/apa find apartments for rent.
# https://sfbay.craigslist.org/search/sub finds sublets.
# You only need the last 3 letters of the URLs.
CRAIGSLIST_HOUSING_SECTION = 'apa'

## System settings

# How long we should sleep between scrapes of Craigslist.
# Too fast may get rate limited.
# Too slow may miss listings.
# SLEEP_INTERVAL = 20 * 60 # 20 minutes

SLEEP_INTERVAL = 20 # 20 seconds

# Which slack channel to post the listings into.
SLACK_CHANNEL = "#housing"

# The token that allows us to connect to slack.
# Should be put in private.py, or set as an environment variable.
# SLACK_TOKEN = os.getenv('SLACK_TOKEN', "")

with open('auth_slack.json') as data_file:    
    slackAuthentication = json.load(data_file)

SLACK_TOKEN = slackAuthentication['TOKEN']

# DB Location
DB_URI = "sqlite:///listings.db"

# Neighbourhoods shpfile
NEIGHBOURHOOD_MAP = "TorNeighbour.shp"

# Parsed Neighbourhoods file
NEIGHBOURHOOD_File = "neighbourhood.json"

# Any private settings are imported here.
try:
    from private import *
except Exception:
    pass

# Any external private settings are imported from here.
try:
    from config.private import *
except Exception:
    pass