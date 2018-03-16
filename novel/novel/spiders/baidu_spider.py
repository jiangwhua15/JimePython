import scrapy
from novel.items import NovelItem
import re
from scrapy import Request

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    def start_requests(self):
        yield Request('http://www.sogou.com/web?query=圣虚',self.parse)
    def parse(self,response):
        item = NovelItem()
        for sel in response.xpath('//div[contains(@class,"results")]/div[contains(@id,"sogou_vr_")]') :
            #去除搜狗正版小说结果，要钱的不要
            if ''.join(sel.xpath('.//a[contains(@id,"title")]/@href').extract()).find('sogou') < 0 :
                novelInfo = re.findall("作者：(.*)类型：(.*)状态：(.*)简介：(.*)新：",''.join(sel.xpath('.//text()').extract()).replace('\n','').replace("\x20",''))
                # key_tuple = ('author','category','novelstatus','des')
                # d = dict(zip(key_tuple,novelInfo[0]))

                item['author'] = novelInfo[0][0]
                item['category'] = novelInfo[0][1]
                item['novelstatus'] = novelInfo[0][2]
                item['des'] = novelInfo[0][3]
                url = sel.xpath('.//a[contains(@id,"title")]/@href').extract()[0]
                yield item
                yield Request(url,callback=self.get_name)

    def get_name(self,response):
        '''获取小说名称,图片地址'''
        item = NovelItem()
        name = response.xpath('//div[@id="info"]/h1/text()').extract()
        novel_img =  'http://'+response.meta['download_slot'] + ''.join(response.xpath('//div[@id="fmimg"]/img/@src').extract())
        item['name'] = name
        item['novelImg'] = novel_img

        print(item)