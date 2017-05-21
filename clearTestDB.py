from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select

def clearTable():
	db_uri = 'sqlite:///listings.db'
	engine = create_engine(db_uri)

	conn = engine.connect()
	meta = MetaData(engine,reflect=True)
	table = meta.tables['listings']

	## Select * from Listings, printing out all rows.
	select_st = select([table])
	res = conn.execute(select_st)
	for _row in res: print _row


	## Deletes from Listings
	meta = MetaData()
	con = engine.connect()
	trans = con.begin()
	print table.delete()
	con.execute(table.delete())
	trans.commit()

if __name__ == "__main__":
	clearTable()