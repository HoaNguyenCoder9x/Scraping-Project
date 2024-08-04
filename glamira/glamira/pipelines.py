# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


# class GlamiraPipeline:
#     def process_item(self, item, spider):
#         return item


import pymongo 
from itemadapter import ItemAdapter
from glamira.items import AppleWatchCaseSpider_Item, BraceletsSpider_Item, Earring_Item, Necklaces_Item, RingSpider_Item
# from scrapy.exceptions import DropItem

class transform:
    # def process_item(self, item, spider):
    #     if isinstance(item, AppleWatchCaseSpider_Item):
    #         return self.process_item_AppleWatchCase(item, spider)
    #     elif isinstance(item, BraceletsSpider_Item):
    #         return self.process_item_BraceletsSpider(item, spider)


    #     # else:
    #     #     return item
        
    # def process_item_AppleWatchCase(self, item, spider):
    #     adapter = ItemAdapter(item)
    #     adapter['price'] = float(adapter['price'].replace('$','').replace(',','/.'))
    #     adapter['metal_weight_gr'] = float(adapter['metal_weight_gr'].replace(',','.'))
    #     adapter['category'] = adapter['page_link'].split('/')[3]
        
    #     return item 

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        adapter['price'] = float(adapter['price'].replace('$','').replace(',',''))
        adapter['category'] = adapter['page_link'].split('/')[3]
        
        return item 



class MongoPipeline:
    collection_name = "scrapy_items"

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db


    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DATABASE", "items"),
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    # def process_item(self, item, spider):
    #     self.db[self.collection_name].insert_one(ItemAdapter(item).asdict())
    #     return item


    def process_item(self, item, spider):
        # Define the query to check if the document exists

        query = {'product_no': item['product_no']}
        
        # Check if the document exists
        if self.db[self.collection_name].find_one(query):
            spider.log(f"Item already exists: {item}")
        else:
            # If not, insert the new item
            self.db[self.collection_name].insert_one(dict(item))
            spider.log(f"Item inserted: {item}")
        return item
         


from pathlib import PurePosixPath
from urllib.parse import urlparse

from scrapy.pipelines.images import ImagesPipeline



class MyImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        return PurePosixPath(urlparse(request.url).path).name
    
    

