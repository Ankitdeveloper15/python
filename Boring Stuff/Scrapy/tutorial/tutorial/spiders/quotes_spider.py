import scrapy
from ..items import TutorialItem


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    pageNumber = 2
#    def start_requests(self):
    start_urls = [
    'http://quotes.toscrape.com/page/1/'
#           'http://quotes.toscrape.com/page/1/',
#          'http://quotes.toscrape.com/page/2/',
    ]
        #for url in urls:
            #yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        items = TutorialItem()
        all_quotes = response.css('div.quote')

        for quote in all_quotes:

            title = quote.css('.text::text').extract()
            author = quote.css('.author::text').extract()
            tag = quote.css('div.tags .tag::text').extract()
            #titleget = response.css('title::text').get()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            #yield {'title': title, 'author':author, 'tags':tag}
            yield items

        #next_page = response.css('li.next a::attr(href)').get()
        next_page = 'http://quotes.toscrape.com/page/'+str(self.pageNumber)+'/'
        print('Next Page is: ',next_page)
        if self.pageNumber <= 10:
            self.pageNumber += 1
            yield response.follow(next_page, callback=self.parse)

        
        
        


##textspider = QuoteSpider()
##yieldvalue = textspider.parse()
