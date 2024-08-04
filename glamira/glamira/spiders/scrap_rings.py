

# Handling import sibling module
import sys
sys.path.append("..")



from typing import Any
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.utils.reactor import install_reactor
from scrapy.http import Response
# from glamira.items import AppleWatchCaseSpider_Item
from glamira.items import RingSpider_Item



class RingSpider(scrapy.Spider):
    name = "RingSpider"
    custom_settings = {
        
        "IMAGES_STORE" : "image_folder/Rings",
        # "FEEDS" : {"data/RingSpider.jsonl" : {"format" : "jsonl", "overwrite":True}}

    }



    allowed_domains = ["www.glamira.com","cdn-media.glamira.com"]
    start_urls =    ["https://www.glamira.com/diamond-rings/"]
    install_reactor("twisted.internet.asyncioreactor.AsyncioSelectorReactor")
    
    def parse(self, response):
        
        # self.logger.info("********* NEW USER AGENT ****************")
        # self.logger.info("NEW USER AGENT %s", response.request.headers['User-Agent'])  

        
        self.page_request = response.request.url
        products = response.css('div.product-item-details a')
        for product in products:
            self.page_request = response.request.url
            self.product_link = product.css('::attr(href)').get()
            yield response.follow(self.product_link, callback=self.parse_product_details       )   # , headers=get_random_header(header_list) 
        


        # Loop next page
        link_extractor = LinkExtractor(restrict_text= ['Next Page']) 
        links = link_extractor.extract_links(response)
        
        for link in links:
            self.next_page = link.url
            if self.next_page is not None:
                yield response.follow(self.next_page, callback=self.parse    )  #, headers=get_random_header(header_list)   


    def parse_product_details(self, response: Response, **kwargs: Any) -> Any:
        RingSpider_item = RingSpider_Item()
        
        images = response.css('.gallery-img::attr(srcset)').getall()
       
        images_list = []
        for each in images:    
            real_image = each.split(' ')[2]
            images_list.append(real_image)

        RingSpider_item['image_urls'] = images_list
        RingSpider_item['page_link'] = self.page_request 
        RingSpider_item['product_link'] =  response.request.url
        RingSpider_item['product_name'] = response.css('.base::text').get()
        RingSpider_item['price'] =response.css('.price::text').get()
        RingSpider_item['product_description'] =response.css('.product-description::text').get()
        RingSpider_item['product_no'] = response.css('#product-detail-container .detail-value span::text').getall()[0]
        
        RingSpider_item['center_stone'] = response.css('.detail-value span.Stone::text').get()

              
        yield RingSpider_item