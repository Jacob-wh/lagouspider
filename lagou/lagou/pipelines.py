# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import pymysql
class LagouPipeline(object):
    def process_item(self, item, spider):
        companyName = item["companyName"][0]
        positionName =  item["positionName"][0]
        positionIntro = ''.join(str(i) for i in item["positionIntro"])
        positionLabel = ','.join(str(i) for i in item["positionLabel"])
        workResponsibility = ''.join(str(i) for i in item["workResponsibility"])
        workResponsibility = workResponsibility.replace("，",",").replace("。",".").replace("：",":").replace("【","[").replace("】","]").replace("；",";").replace("、",",").replace(" " , "")
        positionWelfare = ','.join(str(i) for i in item["positionWelfare"])
        workAddress = ''.join(str(i) for i in item["workAddress"])
        workAddress = workAddress.replace("查看地图","")
        db = pymysql.connect(host = "localhost" , user = "root" , password = "" , db = "lagou" , port = 3306)
        cur = db.cursor();
        sql = "insert into position (companyName , positionName , positionIntro , positionLabel , workResponsibility , positionWelfare , workAddress) values('%s','%s', '%s','%s', '%s','%s','%s')" %(companyName , positionName , positionIntro , positionLabel , workResponsibility , positionWelfare , workAddress)
        print(sql);
        # sql = "insert into position (companyName , positionName , positionIntro , positionLabel , workResponsibility , positionWelfare , workAddress) values('s','s', 's','s', 's','s','s')";
        try:
            cur.execute(sql);
            db.commit();
        except Exception  as e:
            print("chucuole")
            db.rollback();
        finally:
            db.close();
        return item
