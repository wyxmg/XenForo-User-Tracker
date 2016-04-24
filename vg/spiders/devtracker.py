import scrapy
from vg.items import VgItem
from urlparse import urljoin

class DevtrackerSpider(scrapy.Spider):
    name = "devtracker"
    allowed_domains = ["forums.vainglorygame.com"]
    start_urls = (
        'http://forums.vainglorygame.com/index.php?search/member&user_id=3326',
		'http://forums.vainglorygame.com/index.php?search/member&user_id=913',
    )


    def parse(self, response):
        for sel in response.xpath('//h3[@class="title"]'):
            item = VgItem()
            item['title'] = sel.xpath('a/text()').extract()[0]
            item['_id'] = urljoin('forums.vainglorygame.com/', ''.join(sel.xpath('a/@href').extract()[0])) 
            item['desc'] = sel.xpath('../../blockquote/a/text()').extract()[0]
            item['user'] = sel.xpath('	../../div[@class="meta"]/a[@class="username"]/text()').extract()[0]
			#Xenforo shows newest posts in a different format that older posts, so this checks to see which format the post is using, and then gathers data from the correct XPath location
            if (sel.xpath('../../div[@class="meta"]/abbr[@data-datestring]/@data-datestring').extract()) != []:
				item['date'] = (sel.xpath('../../div[@class="meta"]/abbr[@data-datestring]/@data-datestring').extract()[0])
            else:
				item['date'] = sel.xpath('../../div[@class="meta"]/span[@class="DateTime"]/text()').extract()[0]
            yield item
			