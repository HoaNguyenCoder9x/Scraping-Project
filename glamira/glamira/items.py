# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field



class AppleWatchCaseSpider_Item(Item):
    image_urls = Field()
    images = Field()
    page_link = Field()
    product_link = Field()
    product_name = Field()
    price = Field()

    product_description = Field()
    product_no = Field()
    case = Field()
    bracelet = Field()
    case_thickness_mm = Field()
    case_size = Field()
    wrist_size = Field()
    metal_weight_gr = Field()
    compatibility = Field()

class RingSpider_Item(Item):
    image_urls = Field()
    images = Field()
    page_link = Field()
    product_link = Field()
    product_name = Field()
    price = Field()
    product_description = Field()
    
    product_no = Field()
    center_stone = Field()
    # stone_shape = Field()
    # stone_total_carat = Field()
    # center_stone_diameter = Field()
     
class Necklaces_Item(Item):
    image_urls = Field()
    images = Field()
    page_link = Field()
    product_link = Field()
    product_name = Field()
    price = Field()
    product_description = Field()
    
    product_no = Field()
    center_stone = Field()
    chain = Field()



class Earring_Item(Item):
    image_urls = Field()
    images = Field()
    page_link = Field()
    product_link = Field()
    product_name = Field()
    price = Field()
    product_description = Field()
    
    product_no = Field()
    center_stone = Field()
    stone_color_metal = Field()
        

class BraceletsSpider_Item(Item):
    image_urls = Field()
    images = Field()
    page_link = Field()
    product_link = Field()
    product_name = Field()
    price = Field()
    product_description = Field()
    
    product_no = Field()
    center_stone = Field()
