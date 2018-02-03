# -*- coding: utf-8 -*-
import scrapy

from scrapy import Request

from lagou import settings

import time

from lagou.items import LagouItem

from scrapy import Request , Spider
# //*[@id="s_position_list"]/ul/li[14]/div[1]/div[1]/div[1]/a/h3
class LagouSpider(scrapy.Spider):
    name = 'LaGou'
    allowed_domains = ['lagou.com']
    start_urls = ['https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='];

    # def start_requests(self):
    #     start_urls = 'https://www.lagou.com/jobs/list_python';
    #     print('重写的方法////////////////////////////')
    #     header = {
    #         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36",
    #     }
    #     yield scrapy.Request(url=start_urls , headers=header)

    def parse(self, response):
        print("访问成功了，，，，，，，，，，，，，")
        # print(response.body.decode());
        # positionName = response.xpath("//*[@id='s_position_list']/ul/li/div/div/div/a/h3/text()").extract();
        # print(positionName);
        positionUrl = response.xpath("//*[@id='s_position_list']/ul/li/div/div/div/a[@class='position_link']/@href").extract();
        # print(positionUrl)
        # yield Request(positionUrl , callback=self.parse2 , encoding='utf-8')
        for url in positionUrl:
            # print(url);
            time.sleep(5);
            yield Request(url , callback=self.parse2)
            

    def parse2(self , response):
        
        print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
        Item = LagouItem();
        Item["positionName"] = response.xpath("/html/body/div[2]/div/div[1]/div/span/text()").extract();
        Item["positionIntro"] = response.xpath("/html/body/div[2]/div/div[1]/dd/p[1]/span/text()").extract();
        Item["positionHead"] = response.xpath("/html/body/div[2]/div/div[1]/dd/ul/li/text()").extract();
        Item["workResponsibility"] = response.xpath("//*[@id='job_detail']/dd[2]/div/ul[1]/li/p/text()").extract();
        Item["workRequire"] = response.xpath("//*[@id='job_detail']/dd[2]/div/ul[2]/li/p/text()").extract();
        Item["positionWelfare"] = response.xpath("//*[@id='job_detail']/dd[2]/div/ul[3]/li/p/text()").extract();
        Item["workAddress"] = response.xpath("//*[@id='job_detail']/dd[3]/div[1]/a/text()").extract();
        yield Item;