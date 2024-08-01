# Handling import sibling module
import sys
sys.path.append("..")


# Run the spider with the internal API of Scrapy:
from scrapy.crawler import Crawler, CrawlerProcess
from scrapy.utils.project import get_project_settings

# For Spider 
from glamira.spiders.scrap_apple_watch import AppleWatchCaseSpider
from glamira.spiders.scrap_rings import RingSpider
from glamira.spiders.scrap_bracelets import BraceletsSpider
from glamira.spiders.scrap_earrings import EarringSpider
from glamira.spiders.scrap_necklaces import NecklacesSpider




# For loggind handling
import logging
from scrapy.utils.log import configure_logging
import os

from datetime import datetime




# LOGGING
log_file_path = 'scrapy_summary_logs.txt'
if os.path.exists(log_file_path):
    os.remove(log_file_path)

configure_logging(install_root_handler=False)
logging.basicConfig(
    filename=log_file_path,
    format='%(levelname)s: %(message)s',
    level=logging.INFO
    # filemode='w'  # Overwrite mode
)


custom_settings={

    "AUTOTHROTTLE_ENABLED" : True,
    "AUTOTHROTTLE_START_DELAY" : 0.5,
    "AUTOTHROTTLE_MAX_DELAY" : 60,
    "AUTOTHROTTLE_TARGET_CONCURRENCY" : 2,
    # "AUTOTHROTTLE_DEBUG" : True,
    # "DOWNLOAD_DELAY": 2
    # "CONCURRENT_REQUESTS_PER_IP" : 16,
    # "CONCURRENT_REQUESTS" : 100,

    "RETRY_ENABLED" : True,
    "RETRY_HTTP_CODES" : [500, 502, 503, 504, 522, 524, 408, 403],
    "RETRY_TIMES" : 5,
    "RETRY_BACKOFF_BASE" : 1,
    "DOWNLOADER_MIDDLEWARES" : {'glamira.middlewares.CustomRetryMiddleware': 550 }  ,
    "ITEM_PIPELINES" : {"scrapy.pipelines.images.ImagesPipeline": 1}
    }



settings = get_project_settings()
# settings['DOWNLOAD_DELAY'] = 2
 

# CALL SPIDER
crawler_apple_watch_case = Crawler(
    AppleWatchCaseSpider,
    settings=custom_settings
    # settings={
    #     **settings,
    #     "FEEDS": {
    #         "data/apple_watch_case.json": {"format": "jsonl",  "overwrite": True},
        
    #     },

    # },
)
 
crawler_rings = Crawler(
    RingSpider,
    settings=custom_settings
)

crawler_bracelets = Crawler(
    spidercls=BraceletsSpider,
    settings=custom_settings
)

crawler_earring = Crawler(
    EarringSpider,
    settings=custom_settings
)

crawler_necklaces = Crawler(
    NecklacesSpider,
    settings=custom_settings
)


# CHECK IF CURRENT FILE 
if __name__ == '__main__':
    # SETTING


    start_time = datetime.now()


    # Run multi spider in one proccess
    process = CrawlerProcess(settings)
    # process = CrawlerProcess(settings={**get_project_settings(), **custom_settings})


    process.crawl(crawler_apple_watch_case)
    process.crawl(crawler_rings)
    process.crawl(crawler_necklaces)
    process.crawl(crawler_earring)
    process.crawl(crawler_bracelets)



    process.start()

    # Logging time
    end_time = datetime.now()
    logging.info("Start Time %s",start_time)
    logging.info("End Time %s",end_time)
    logging.info("Total Run Time %s",end_time - start_time  )
