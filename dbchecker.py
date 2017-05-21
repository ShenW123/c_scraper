from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.orm import sessionmaker

from dateutil.parser import parse

import settings

def addResultsDB(myResults):
	engine = create_engine(settings.DB_URI, echo=False)

	Base = declarative_base()

	class Listing(Base):
		"""
		A table to store data on craigslist listings.
		"""
		__tablename__ = 'listings'

		id = Column(Integer, primary_key=True)
		link = Column(String, unique=True)
		cl_id = Column(Integer, unique=True)
		created = Column(DateTime)
		geotag = Column(String)
		lat = Column(Float)
		lon = Column(Float)
		name = Column(String)
		price = Column(Float)
		location = Column(String)
		area = Column(String)

	Base.metadata.create_all(engine)

	Session = sessionmaker(bind=engine)
	session = Session()

	uniqueResults = []
	duplicateResults = 0
	for result in myResults:
		# Create the listing object.
		listing = Listing(
			link=result["url"],
			cl_id=result["id"],
			created=parse(result["datetime"]),
			lat=result["geotag"][0],
			lon=result["geotag"][1],
			name=result["name"],
			price=float(result["price"][1:]),
			location=result["where"],
			area=result["area"]
		)
		try:
			session.add(listing)
			session.commit()
			uniqueResults.append(result)
		except:
			duplicateResults = duplicateResults + 1
	if duplicateResults > 0:
		print "There was %d duplicates!" % duplicateResults
	return uniqueResults