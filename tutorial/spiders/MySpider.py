import scrapy


class MySpider(scrapy.Spider):
    name = "myspider"
    start_urls = [
        "http://voce.serpro/",
    ]

    def parse(self, response):
        # We want to inspect one specific response.
        if ".org" in response.url:
            from scrapy.shell import inspect_response
            inspect_response(response, self)

        # Rest of parsing code.