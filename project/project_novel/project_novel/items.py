# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjectNovelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Title = scrapy.Field()
    Author = scrapy.Field()
    Score = scrapy.Field()
    Publishing_house = scrapy.Field()
    Year_of_publication = scrapy.Field()
    Number_of_pages = scrapy.Field()
    Price = scrapy.Field()
    ISBN = scrapy.Field()
    Brief_introduction = scrapy.Field()

