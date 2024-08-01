

# Handling import sibling module
import sys
sys.path.append("..")



from typing import Any
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.utils.reactor import install_reactor
from scrapy.http import Response
from glamira.items import BraceletsSpider_Item




class BraceletsSpider(scrapy.Spider):
    name = "BraceletsSpider"
    custom_settings = {
        
        "IMAGES_STORE" : "image_folder/BraceletsSpider",
        "FEEDS" : {"data/BraceletsSpider.jsonl" : {"format" : "jsonl", "overwrite":True}}
    }
 

    allowed_domains = ["www.glamira.com","cdn-media.glamira.com"]
    start_urls =    ["https://www.glamira.com/bracelets/"]
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
        BraceletsSpider_item = BraceletsSpider_Item()
        
        images = response.css('.gallery-img::attr(srcset)').getall()
       
        images_list = []
        for each in images:    
            real_image = each.split(' ')[2]
            images_list.append(real_image)


        # yield {
        #     # General information
        #     'page_link' : self.page_request ,
        #     'product_link': response.request.url,
        #     'product_name' :  response.css('.base::text').get(),
        #     'price' :  response.css('.price::text').get(),  
        #     'product_img' : images_list,

        #     # Customize property by product type
        #     'product_description' : response.css('.product-description::text').get(),
        #     'product_no' :  response.css('#product-detail-container .detail-value span::text').getall()[0],
        #     'case' : response.css('#product-detail-container .detail-value span::text').getall()[1],
        #     'bracelet' : response.css('#product-detail-container .detail-value span::text').getall()[2],
        #     'case_thickness_mm' : response.css('#product-detail-container .detail-value span::text').getall()[3],
        #     'case_size' : response.css('#product-detail-container .detail-value span::text').getall()[4],
        #     'wrist_size' : response.css('#product-detail-container .detail-value span::text').getall()[5],
        #     'metal_weight_gr' : response.css('#product-detail-container .detail-value span::text').getall()[6],
        #     'compatibility' : response.css('#product-detail-container .detail-value span::text').getall()[7],
            

        # }
        BraceletsSpider_item['image_urls'] = images_list
        BraceletsSpider_item['page_link'] = self.page_request 
        BraceletsSpider_item['product_link'] =  response.request.url
        BraceletsSpider_item['product_name'] = response.css('.base::text').get()
        BraceletsSpider_item['price'] =response.css('.price::text').get()
        BraceletsSpider_item['product_description'] =response.css('.product-description::text').get()
        BraceletsSpider_item['product_no'] = response.css('#product-detail-container .detail-value span::text').getall()[0]
        
        BraceletsSpider_item['center_stone'] = response.css('.detail-value span.Stone::text').get()
        

        # BraceletsSpider_item['chain'] = response.css('#product-detail-container .value::text').getall()[15]
        
     
              
        yield BraceletsSpider_item