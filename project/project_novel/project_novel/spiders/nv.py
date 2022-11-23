import scrapy
from project_novel.items import ProjectNovelItem
class NvSpider(scrapy.Spider):
    name = 'nv'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start=0&type=T']

    base_url = "https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start="
    end = "&type=T"
    start = 0
    def parse(self, response):
        a_list = response.xpath('//div[@class="info"]/h2/a')
        for a in a_list:
            url = a.xpath('./@href').extract_first()
            title = a.xpath('./@title').extract_first()
            yield scrapy.Request(url = url,callback = self.parse_second,meta={'title':title})

            if self.start < 1000 :
                self.start = self.start + 20
                url = self.base_url + str(self.start) + self.end
                yield scrapy.Request(url=url,callback=self.parse)

    def parse_second(self,response):
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        #只有标题、评分、简介不用content     不同的小说的content不同所以split要定义
        title = response.meta["title"]
        score  = response.xpath('//div[@class="rating_self clearfix"]/strong/text()').extract_first()

        content = response.xpath('//div[@id="info"]').extract_first()
        if "作者" in content :
            author = content.split("作者")[1].split("</a>")[0].split(">")[2]
        else :
            author = ""
        if "出版社:" in content :
            Publishing_house  = content.split("出版社:")[1].split("</a>")[0].split(">")[2]
        else:
            Publishing_house = ""
        if "出版年:" in content :
            Year_of_publication  = content.split("出版年:")[1].split("<br>")[0].split(">")[1].strip(' ')
        else:
            Year_of_publication = ""
        if "页数:" in content :
            number_of_pages  = content.split("页数:")[1].split("<br>")[0].split(">")[1].strip(' ')
        else:
            number_of_pages = ""
        if "定价:" in content:
            Price  = content.split("定价:")[1].split("<br>")[0].split(">")[1].strip(' ')
        else:
            Price = ""
        if "ISBN:" in content :
            ISBN  = content.split("ISBN:")[1].split("<br>")[0].split(">")[1].strip(' ')
        else:
            ISBN = ""
        
        #简介部分
        intro_list = response.xpath('//div[@class="intro"]')
        Brief_introduction = ''
        for intro in intro_list:
            p_list = intro.xpath('.//p')
            for p in p_list:
                Brief_introduction += str(p.xpath('./text()').extract_first())

        novel = ProjectNovelItem(Title=title,Author=author,Score=score,
        Publishing_house=Publishing_house,Year_of_publication=Year_of_publication,Number_of_pages=number_of_pages,Price=Price,
        ISBN=ISBN,Brief_introduction=Brief_introduction)

        yield novel
