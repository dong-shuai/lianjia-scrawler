from peewee import *
import datetime
import settings


if settings.DBENGINE.lower() == 'mysql':
	database = MySQLDatabase(
		settings.DBNAME,
		host=settings.DBHOST,
		port=settings.DBPORT,
		user=settings.DBUSER,
		passwd=settings.DBPASSWORD,
		charset='utf8',
		use_unicode=True,
	)

elif settings.DBENGINE.lower() == 'sqlite3':
	database = SqliteDatabase(settings.DBNAME)

elif settings.DBENGINE.lower() == 'postgresql':
	database = PostgresqlDatabase(
		settings.DBNAME,
		user=settings.DBUSER,
		password=settings.DBPASSWORD,
		host=settings.DBHOST,
		charset='utf8',
		use_unicode=True,
	)

else:
	raise AttributeError("Please setup datatbase at settings.py")

class BaseModel(Model):
    class Meta:
        database = database

class Community(BaseModel):
	id 			= BigIntegerField(primary_key=True)
	title 		= CharField(null=True)
	link 		= CharField(unique=True)
	district 	= CharField(null=True)
	bizcircle 	= CharField(null=True)
	tagList 	= CharField(null=True)
	onsale 		= CharField(null=True)
	onrent 		= CharField(null=True)
	year        = CharField(null=True)
	housetype   = CharField(null=True)
	cost        = CharField(null=True)
	service		= CharField(null=True)
	company     = CharField(null=True)
	building_num= CharField(null=True)
	house_num   = CharField(null=True)
	price   	= CharField(null=True)
	validdate 	= DateTimeField(default=datetime.datetime.now)

class Houseinfo(BaseModel):
	houseID 	= CharField(primary_key=True)
	title 		= CharField(null=True)
	link 		= CharField(null=True)
	community 	= CharField(null=True)
	years 		= CharField(null=True)
	housetype 	= CharField(null=True)
	square 		= CharField(null=True)
	direction 	= CharField(null=True)
	floor 		= CharField(null=True)
	taxtype 	= CharField(null=True)
	totalPrice 	= CharField(null=True)
	unitPrice 	= CharField(null=True)
	followInfo 	= CharField(null=True)
	decoration 	= CharField(null=True)
	validdate 	= DateTimeField(default=datetime.datetime.now)

class Hisprice(BaseModel):
	houseID 	= CharField
	totalPrice 	= CharField
	date 		= DateTimeField(default=datetime.datetime.now)

	class Meta:
		primary_key = CompositeKey('houseID', 'totalPrice')

class Sellinfo(BaseModel):
	houseID 	= CharField(primary_key=True)
	title 		= CharField(null=True)
	link 		= CharField(null=True)
	community 	= CharField(null=True)
	years 		= CharField(null=True)
	housetype 	= CharField(null=True)
	square 		= CharField(null=True)
	direction 	= CharField(null=True)
	floor 		= CharField(null=True)
	status 		= CharField(null=True)
	source 		= CharField(null=True)
	totalPrice 	= CharField(null=True)
	unitPrice 	= CharField(null=True)
	dealdate 	= CharField(null=True)
	updatedate 	= DateTimeField(default=datetime.datetime.now)

class Rentinfo(BaseModel):
	houseID 	= CharField(primary_key=True)
	title 		= CharField(null=True)
	link 		= CharField(null=True)
	region 		= CharField(null=True)
	zone 		= CharField(null=True)
	meters 		= CharField(null=True)
	other 		= CharField(null=True)
	subway 		= CharField(null=True)
	decoration 	= CharField(null=True)
	heating 	= CharField(null=True)
	price 		= CharField(null=True)
	pricepre 	= CharField(null=True)
	updatedate 	= DateTimeField(default=datetime.datetime.now)

def database_init():
    database.connect()
    database.create_tables([Community, Houseinfo, Hisprice, Sellinfo, Rentinfo], safe=True)
    database.close()
