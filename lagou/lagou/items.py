# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    companyName = scrapy.Field();
    positionName = scrapy.Field();
    positionIntro = scrapy.Field();
    positionLabel = scrapy.Field();
    workResponsibility = scrapy.Field();
    positionWelfare = scrapy.Field();
    workAddress = scrapy.Field();
