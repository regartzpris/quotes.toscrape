import scrapy
from ..items import QuoteItem


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    start_urls = ['http://quotes.toscrape.com/']

# name,starts_urls,parse is must name
    def parse(self,response):
        # title = response.css('title::text').extract()
        # yield {'titleatext': title}

        items = QuoteItem()
        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            # yield {
            #     'title':title,
            #     'author': author,
            #     'tag' : tag
            # }
            items['title'] =title
            items['author'] = author
            items['tag'] = tag

            yield items


