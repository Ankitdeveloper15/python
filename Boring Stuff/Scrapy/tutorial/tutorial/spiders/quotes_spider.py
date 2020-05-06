import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    
#    def start_requests(self):
    start_urls = [
    'http://quotes.toscrape.com'
#           'http://quotes.toscrape.com/page/1/',
#          'http://quotes.toscrape.com/page/2/',
    ]
        #for url in urls:
            #yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        title = response.css('title::text').extract()
        yield {'titletext': title}
