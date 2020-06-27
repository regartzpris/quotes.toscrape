# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# kila - extracted data > temporay container(items) => storing database so programm not getting err
import scrapy


# class QuoteItem(scrapy.Item): -> class  asli - kila
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class QuoteItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()
