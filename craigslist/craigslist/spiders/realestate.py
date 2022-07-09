import itertools
import scrapy
from ..items import CraigslistItem


class RealestateSpider(scrapy.Spider):
    name = 'realestate'
    allowed_domains = ['newyork.craigslist.org']
                       
    start_urls = ['https://newyork.craigslist.org/search/rea']

    def parse(self, response):
        allAds = response.xpath('//li[@class="result-row"]')
        # firstAd = allAds[0]
        # print(firstAd.xpath('/div/h3/a/text()'))
        # index = 0

        for ad in allAds:
           # index += 1
            title = ad.css('a.result-title.hdrlnk::text').get()
            price= ad.css('span.result-price::text').get()
            link = ad.css("a::attr(href)").get()
            id = ad.css("a::attr(data-id)").get()

            items = CraigslistItem()

           
            
            items['link'] = link 
            items['price'] = price
            items['title'] = title 
            items['id'] = id  

            yield items
        #searchform > div.search-legend.bottom > div.paginator.buttongroup.firstpage > span.buttons > a.button.next
        next_page = response.css('a.button.next').attrib['href']
        max_item = int(response.css('span.rangeTo::text').get())
        print(next_page)
        if max_item < 480:
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)
