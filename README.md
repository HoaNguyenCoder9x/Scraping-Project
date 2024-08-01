# Scraping-Project
Scrap data from website https://www.glamira.com/

## Description
Project scrap all data on webpage Glamira category
 * Ring
 * Necklace
 * Earring
 * Apple Watch Case 






## How to use

1. Git clone project
2. chmod +x run.sh ( allow file execute permisson )
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



> Using CrawlerProcess to run multi spiders in one process, it takes ~ 10hrs to scrap 10Gbs from website

