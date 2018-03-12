import scrapy
import re
from scrapy import Request
class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    def start_requests(self):
        yield Request('http://www.sogou.com/web?query=圣虚',self.parse)
    def parse(self,response):
        for sel in response.xpath('//div[contains(@class,"results")]/div[contains(@id,"sogou_vr_")]') :
            #去除搜狗正版小说结果，要钱的不要
            if len(sel.xpath('.//img[contains(@class,"vr_authico")]').extract()) == 0  :
                print(sel.xpath('.//a[contains(@id,"title")]/@href').extract())
                #print(sel.xpath('.//div[contains(@class,"str-box")]'))
                #print(''.join(sel.xpath('.//text()').extract()))
                print(re.findall("作者：(.*)类型：(.*)状态：(.*)简介：(.*)新：",''.join(sel.xpath('.//text()').extract()).replace('\n','').replace(' ','')))

