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
# 2' setting QuotePipeline class below

import mysql.connector


# class QuotePipeline:  -> kila - class asli
#     def process_item(self, item, spider):
#         return item

class QuotePipeline (object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    # connection to database
    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='kila23',
            database='quote_db'

        )
        self.curr = self.conn.cursor()

        # create database

    def create_table(self):
        self.curr.execute ("""DROP TABLE IF EXISTS quote_db""")
        self.curr.execute ("""create table quote_db(
                title text,
                author text,
                tag text
             )""")

    def process_item(self, item, spider):
        # print("Pipeline :" + item['title'][0])
        self.store_db(item)
        return item

    def store_db(self,item):
        self.curr.execute("""insert into quote_db values (%s,%s,%s)""",(
            item['title'][0],
            item['author'][0],
            item['tag'][0]
        ))
        self.conn.commit()
