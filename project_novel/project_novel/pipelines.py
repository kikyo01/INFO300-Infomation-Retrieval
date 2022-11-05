# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from collections import OrderedDict
import json

class ProjectNovelPipeline:
    def open_spider(self,spider):
        self.fp = open("nv-4.json","w",encoding="utf-8")
    def process_item(self, item, spider):
        item = OrderedDict(item)
        item = json.dumps(item,ensure_ascii=False)
        self.fp.write(str(item))
        return item
    def close_spider(self,spider):
        self.fp.close() 
