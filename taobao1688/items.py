# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Taobao1688DetailItem(scrapy.Item):
    name = scrapy.Field()  #企业名称
    mainproduct = scrapy.Field()  #主营产品

    model = scrapy.Field()  # 经营模式
    officeaddress = scrapy.Field()  # 所在地址

    officemember = scrapy.Field()  # 员工人数
    officearea = scrapy.Field()  # 办公面积

    mainproduct = scrapy.Field()  #主营产品

    model = scrapy.Field()  # 经营模式
    officeaddress = scrapy.Field()  # 所在地址

    officemember = scrapy.Field()  # 员工人数
    officearea = scrapy.Field()  # 办公面积

    salesvolume = scrapy.Field()  # 累计买家数
    volume = scrapy.Field()  # 累计成交数

    repeatsales = scrapy.Field()  #重复采购率
    createtime = scrapy.Field()  #成立时间

    annualturnover = scrapy.Field()  #年营业额
    storecount = scrapy.Field()  #阿里巴巴平台店铺数

    creditrating = scrapy.Field()  # 信用等级
    mainmarket = scrapy.Field()  #主要市场

    maincustomer = scrapy.Field()  #主要客户
    storagearea = scrapy.Field()  # 仓储面积

    storageaddress = scrapy.Field()  # 仓储地址
    contactsnumber = scrapy.Field()  # 联系电话
