import scrapy


class VgItem(scrapy.Item):
	title = scrapy.Field()
	_id = scrapy.Field()
	desc = scrapy.Field()
	user = scrapy.Field()
	date = scrapy.Field()
