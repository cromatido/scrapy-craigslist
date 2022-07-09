import scrapy


class RealestateSpider(scrapy.Spider):
    name = 'realestate'
    allowed_domains = ['newyork.craigslist.org']
    start_urls = ['http://newyork.craigslist.org/']

    def parse(self, response):
        pass
