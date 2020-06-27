# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# kila - scraped data  > item containers >json/csv files
# kila - scrapped data > item container > pipeline>sql/mongodb database


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# class QuotePipeline:  -> kila - class asli
#     def process_item(self, item, spider):
#         return item
 # ----- kila-----
# 1. enable setting pipeline in setting.py
#2' setting QuotePipeline class below


# class QuotePipeline:  -> kila - class asli
#     def process_item(self, item, spider):
#         return item

class QuotePipeline:
    def process_item(self, item, spider):
        print("Pipeline :" + item['title'][0])
        return item