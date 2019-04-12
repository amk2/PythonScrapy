import scrapy
from scrapy.contrib.loader import ItemLoader
 
class YoutubeVideo(scrapy.Item):
    link = scrapy.Field()

 
class YoutubeChannelLister(scrapy.Spider):
    name = 'youtube-channel-lister'
    youtube_channel = 'LongboardUK'
    start_urls = ["http://www.serpro.gov.br"]
 
    def parse(self, response):
        for sel in response.css("ul#channels-browse-content-grid > li"):
            loader = ItemLoader(YoutubeVideo(), selector=sel)
 
            loader.add_xpath('link', './/h3/a/@href')
            
            yield loader.load_item()