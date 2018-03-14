import scrapy
import re
from urllib.parse import urlparse
from scrapy import Request
class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    def start_requests(self):
        yield Request('http://www.sogou.com/web?query=圣虚',self.parse)
    def parse(self,response):
        for sel in response.xpath('//div[contains(@class,"results")]/div[contains(@id,"sogou_vr_")]') :
            #去除搜狗正版小说结果，要钱的不要
            #if len(sel.xpath('.//img[contains(@class,"vr_authico")]').extract()) == 0  :
            if ''.join(sel.xpath('.//a[contains(@id,"title")]/@href').extract()).find('sogou') < 0 :
                novelInfo = re.findall("作者：(.*)类型：(.*)状态：(.*)简介：(.*)新：",''.join(sel.xpath('.//text()').extract()).replace('\n','').replace("\x20",''))
                key_tuple = ('author','category','novelstatus','des')
                d = dict(zip(key_tuple,novelInfo[0]))

                url = sel.xpath('.//a[contains(@id,"title")]/@href').extract()[0]
                d['domain'] = urlparse(url).netloc
                yield Request(url,self.get_name,meta=d)

    def get_name(self,reponse):
        print(reponse.meta)
