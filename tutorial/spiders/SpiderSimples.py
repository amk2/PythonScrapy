import scrapy

class SpiderSimples(scrapy.Spider):
    name = 'meuspider'

    def start_requests(self):
        return [scrapy.Request('http://psds.portalcorporativo.serpro/psds/')]

    def parse(self, response):
        self.log('Visitei o site: %s' % response.url)