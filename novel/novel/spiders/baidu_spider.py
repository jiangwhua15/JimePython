import scrapy
from ..items import NovelItem
from .threeone import ThreeOne
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
            if ''.join(sel.xpath('.//a[contains(@id,"title")]/@href').extract()).find('sogou') < 0 :
                novelInfo = re.findall("作者：(.*)类型：(.*)状态：(.*)简介：(.*)新：",''.join(sel.xpath('.//text()').extract()).replace('\n','').replace("\x20",''))
                key_tuple = ('author','category','novelstatus','des')
                novelInfo_dict = dict(zip(key_tuple,novelInfo[0]))
                url = sel.xpath('.//a[contains(@id,"title")]/@href').extract()[0]
                pr = urlparse(url)
                novelInfo_dict['scheme'] = pr.scheme
                novelInfo_dict['netloc'] = pr.netloc
                yield Request(url,callback=self.get_name,meta=novelInfo_dict)

    def get_name(self,response):
        '''获取小说名称,图片地址'''
        print(response.meta)
        ThreeOne.get_chapter()
        # item = NovelItem()
        # name = response.xpath('//div[@id="info"]/h1/text()').extract()
        # novel_img =  'http://'+response.meta['download_slot'] + ''.join(response.xpath('//div[@id="fmimg"]/img/@src').extract())
        # item['name'] = name[0]
        # item['novelImg'] = novel_img
        # return item
