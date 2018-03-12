import scrapy
from scrapy import Request
class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    def start_requests(self):
        yield Request('http://www.sogou.com/web?query=飞剑问道',self.parse)
    def parse(self,response):
        i = 1
        for sel in response.xpath('//div[contains(@class,"results")]/div[contains(@id,"sogou_vr_")]') :

            filename = 'sougou'+ str(i)
            with open(filename,'wb') as f:
                f.write(sel.extract().encode())
                #pass
            i += 1
            print(sel.xpath('.//a[contains(@id,"title")]/@href').extract())