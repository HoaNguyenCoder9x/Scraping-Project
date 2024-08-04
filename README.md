# Scraping-Project
Scrap data from website https://www.glamira.com/



## Description
Project scrap all data on webpage Glamira category
 * Ring
 * Necklace
 * Earring
 * Apple Watch Case 
 * Bracelets

> Using CrawlerProcess to run multi spiders in one process, it takes ~ 10hrs to scrap 10Gbs from website

## Prequisite
    
    The pipeline write data into local mongoDB, so you need to set up your own mongoDB and update the property ``` MONGO_URI``` in glamira/glamira/settings.py

    In case you wouldn't like write data into MongoDB, feel free to disable "glamira.pipelines.MongoPipeline" in  glamira/glamira/spiders/production/glamira_dev.py


## How to use

1. Git clone project
2. chmod +x run.sh ( to allow file execute permisson )
3. run ./run.sh 
    * Create .venv 
    * Install neccessary module from requirement.txt
    * exec glamira/glamira/spiders/production/glamira_dev.py

4. 
    * Data and image will be located at glamira/glamira/image_folder and glamira/glamira/data
    * Logfile will be at glamira/glamira/scrapy_summary_logs.txt


Or you can use below command to run each spider:
```
scrapy list -- to list all spiders
scrapy crawl [spider_name] -O data.json --logfile scrapy_log.log
```





## How to test the checkpoint

1. cd to glamira/glamira
2. run ```python3 spiders/production/glamira_dev.py ``` to run parallel spiders
3. Press ``` Ctrl + C ``` ( once ) and wait a bit for spider stop
4. Rerun ```python3 spiders/production/glamira_dev.py ``` to continue scraping
5. Check the ```product_no``` property in data file in glamira/glamira/data to verify
> Spider will continue from the last run, base on glamira/glamira/crawls path checkpoint folder


## Versioning:

28/07/2024:

    1. Build parallel running spider ( 5 spiders )

04/08/2024:

    1. Add function write data scrap from website to mongoDB
    2. Update pip requirements library
    3. Link image with data 
    4. Add checkpoint for resuming scrap data




