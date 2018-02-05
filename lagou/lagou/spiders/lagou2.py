# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy.http import FormRequest
import json
from lagou.items import LagouItem
from scrapy import Request
class Lagou2Spider(scrapy.Spider):
    name = 'lagou2'
    allowed_domains = ['lagou.com']
    # start_urls = ['http://lagou.com/']
    # print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
    def start_requests(self):
        start_urls = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false&isSchoolJob=0';
        print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
        a=[];
        # for i in range(5):
        FormData={
            'first':'false',
            'pn':str(1),
            'kd':'python',
        }
            # FormData = json.dumps(FormData)
        time.sleep(2);
        res = FormRequest(url=start_urls , callback=self.parsePostData , formdata=FormData)
        print(res);
        a.append(res);
        return a;

    def parsePostData(self, response):

        headers = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate, br",
            "Accept-Language":"zh-CN,zh;q=0.9",
            "Cache-Control":"no-cache",
            "Connection":"keep-alive",
            "Host":"www.lagou.com",
            "Pragma":"no-cache",
            "Cookie":'user_trace_token=20180120212822-c98c62b1-fde5-11e7-b08c-525400f775ce; LGUID=20180120212822-c98c689d-fde5-11e7-b08c-525400f775ce; index_location_city=%E5%8C%97%E4%BA%AC; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; _gid=GA1.2.227984683.1517793412; _putrc=A854A48E25B5FAE3; JSESSIONID=ABAAABAAAGFABEFCC20D98600FBFD859ADE83F80F696D0C; login=true; unick=jacob; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1517630016,1517638248,1517793412,1517811697; gate_login_token=d4e4c205b4fac27055b3564b4ae6525aed09d5e894f74c78; LGSID=20180205154749-dd0aa309-0a48-11e8-af71-5254005c3644; TG-TRACK-CODE=search_code; SEARCH_ID=1b9771a2a2d94876bf1daae72fb365c4; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1517818393; LGRID=20180205161313-693477ef-0a4c-11e8-af71-5254005c3644',
            'Host': 'www.lagou.com',
            'Origin': 'https://www.lagou.com',
            'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36"
        }
        jobUrl = json.loads(response.body.decode('utf-8'))["content"]["hrInfoMap"];

        for index in jobUrl:
            time.sleep(2)
            url = "https://www.lagou.com/jobs/%s.html" % index
            yield Request(url , callback=self.parseDetail , headers=headers)
    def parseDetail(self , response):
        print(response.status)
        if response.status == 200:
            Item = LagouItem();
            print("----------------------------------------------------------------------------------------")
            #公司名
            Item["companyName"] = response.xpath("/html/body/div[2]/div/div[1]/div/div[1]/text()").extract();
            #职位名
            Item["positionName"] = response.xpath("/html/body/div[2]/div/div[1]/div/span/text()").extract();
            #职位简介
            Item["positionIntro"] = response.xpath("/html/body/div[2]/div/div[1]/dd/p[1]/span/text()").extract();
            #职位标签
            Item["positionLabel"] = response.xpath("/html/body/div[2]/div/div[1]/dd/ul/li/text()").extract();
            #职位职责
            Item["workResponsibility"] = response.xpath("//*[@id='job_detail']/dd[2]/div/p/text()").extract();
            #职位福利
            # //*[@id="job_detail"]/dd[1]/p
            Item["positionWelfare"] = response.xpath("//*[@id='job_detail']/dd[1]/p/text()").extract();
            # 职位地址
            Item["workAddress"] = response.xpath("//*[@id='job_detail']/dd[3]/div[1]/a/text()").extract();
            yield Item;