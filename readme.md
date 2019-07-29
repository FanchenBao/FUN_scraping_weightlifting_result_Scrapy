## Date
07/21/2019

## Description
This is a practice project for the use of [Scrapy](https://scrapy.org/) to retrieve weightlifting meet results available on [IWF's official website](https://www.iwf.net/). The initial plan was to use **Scrapy** to get all currently available data into a csv file, use such file to populate a database, and then push the database and some front- and back-end code on to heroku as a simple web app for people to easily query weightlifting results. However, this plan is scrapped because populating a local database from the csv file means that the local database has to be exported to the database on heroku, which entails additional hassel. Therefore, this practice project has no further use for the web app. But as a practice of using **Scrapy**, it is still quite valuable.

Building of this probject followed the [Scrapy tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html) almost step by step. If there is any confusion about the code, refer to the tutorial for demonstration and explanation.

## Usage
* Clone the repository
* `cd FUN_scraping_weightlifting_result_Scrapy`
* `pip install -r requirements.txt`
* `cd gather_weightlifting_data`
* `scrapy crawl iwf`
* A file `all_data.csv` will be generated, containing all weightlifting meet results from 1998 till present.