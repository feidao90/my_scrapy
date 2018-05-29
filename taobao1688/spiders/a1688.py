# -*- coding: utf-8 -*-
import scrapy
from ..items import Taobao1688DetailItem

import time

class A1688Spider(scrapy.Spider):
    name = 'a1688'
    allowed_domains = ['1688.com']

    # 设置下载延时
    download_delay = 30
    start_urls = ['https://s.1688.com/company/company_search.htm?keywords=%B8%A3%D6%DD&button_click=top&earseDirect=false&n=y']
    def parse(self,response):
        for sel in response.xpath('//div[@id="sw_mod_searchlist"]/ul/li'):

            item = dict()
            item['name'] = sel.xpath('string(./div[1]/div[2]/div[1]/a[1])').extract()
            item['name'] = item['name'][0] if len(item['name']) > 0 else ''
            item['mainproduct'] = sel.xpath('string(./div[1]/div[2]/div[3]/div[1]/div[1]/a)').extract()
            item['mainproduct'] = item['mainproduct'][0] if len(item['mainproduct']) > 0 else ''
            mainprodoctlist = item['mainproduct'].split('\n')
            item['mainproduct'] = ''.join(mainprodoctlist)

            item['model'] = sel.xpath('string(./div[1]/div[2]/div[3]/div[2]/div[1]/b)').extract()
            item['model'] = item['model'][0] if len(item['model']) > 0 else ''
            item['officeaddress'] = sel.xpath('string(./div[1]/div[2]/div[3]/div[1]/div[2]/a)').extract()
            item['officeaddress'] = item['officeaddress'][0] if len(item['officeaddress']) > 0 else ''

            item['officemember'] = sel.xpath('string(./div[1]/div[2]/div[3]/div[1]/div[3]/a)').extract()
            item['officemember'] = item['officemember'][0] if len(item['officemember']) > 0 else ''
            item['officearea'] = sel.xpath('string(./div[1]/div[2]/div[3]/div[2]/div[3]/a)').extract()
            item['officearea'] = item['officearea'][0] if len(item['officearea']) > 0 else ''

            url = sel.xpath('./div[1]/div[2]/div[3]/div[1]/div[4]/a[3]/@href').extract()
            url = url[0] if len(url) > 0 else ''

            #增加爬虫间隔
            time.sleep(10)
            # yield item
            yield response.follow(url,
                                  method='GET',
                                  meta={'base': item},
                                  dont_filter=True,
                                  callback=self.parse_detail)

    def parse_detail(self,response):
        baseInfo = response.meta['base']

        for sel in response.xpath('//*[@id="site_content"]'):
            item2 = Taobao1688DetailItem()
            item2['name'] = baseInfo['name']
            item2['mainproduct'] = baseInfo['mainproduct']
            item2['model'] = baseInfo['model']
            item2['officeaddress'] = baseInfo['officeaddress']
            item2['officemember'] = baseInfo['officemember']
            item2['officearea'] = baseInfo['officearea']

            item2['volume'] = sel.xpath('string(.//*[@id="J_CompanyTradeCreditRecord"]/ul/li[1]/p[2])').extract()
            item2['volume'] = item2['volume'][0] if len(item2['volume']) > 0 else ''
            item2['salesvolume'] = sel.xpath('string(.//*[@id="J_CompanyTradeCreditRecord"]/ul/li[2]/p[2])').extract()
            item2['salesvolume'] = item2['salesvolume'][0] if len(item2['salesvolume']) > 0 else ''

            item2['repeatsales'] = sel.xpath('string(.//*[@id="J_CompanyTradeCreditRecord"]/ul/li[3]/p[2])').extract()
            item2['repeatsales'] = item2['repeatsales'][0] if len(item2['repeatsales']) > 0 else ''
            item2['createtime'] = sel.xpath('string(//*[@id="site_content"]/div/div/div/div[2]/div/div[2]/div/div[2]/div[2]/table/tbody/tr[1]/td[2]/p/span[1])').extract()
            item2['createtime'] = item2['createtime'][0] if len(item2['createtime']) > 0 else ''

            item2['annualturnover'] = sel.xpath('string(.//*[@id="J_MCA_DepthInspectionTab_product"]/div/ul/li[3]/div[2]/p[2])').extract()
            item2['annualturnover'] = item2['annualturnover'][0] if len(item2['annualturnover']) > 0 else ''
            item2['storecount'] = sel.xpath('string(.//*[@id="J_CompanyDetailInfoList"]/div[2]/table/tbody/tr[2]/td[4])').extract()
            item2['storecount'] = item2['storecount'][0] if len(item2['storecount']) > 0 else ''

            item2['creditrating'] = sel.xpath('//*[@id="site_content"]/div/div/div/div[2]/div/div[2]/div/div[1]/div/div[1]/h1/a[2]/text()').extract()
            item2['creditrating'] = item2['creditrating'][0] if len(item2['creditrating']) > 0 else ''
            item2['mainmarket'] = sel.xpath('string(.//*[@id="J_CompanyDetailInfoList"]/div[2]/table/tbody/tr[2]/td[2])').extract()
            item2['mainmarket'] = item2['mainmarket'][0] if len(item2['mainmarket']) > 0 else ''

            item2['maincustomer'] = sel.xpath('string(.//*[@id="J_CompanyDetailInfoList"]/div[2]/table/tbody/tr[1]/td[4])').extract()
            item2['maincustomer'] = item2['maincustomer'][0] if len(item2['maincustomer']) > 0 else ''
            item2['storagearea'] = sel.xpath('string(.//*[@id="J_CompanyDetailInfoList"]/div[2]/table/tbody/tr[2]/td[4])').extract()
            item2['storagearea'] = item2['storagearea'][0] if len(item2['storagearea']) > 0 else ''

            item2['storageaddress'] = sel.xpath('string(.//*[@id="J_CompanyDetailInfoList"]/div[2]/table/tbody/tr[1]/td[2])').extract()
            item2['storageaddress'] = item2['storageaddress'][0] if len(item2['storageaddress']) > 0 else ''
            item2['contactsnumber'] = sel.xpath('string(.//*[@id="J_COMMON_CompanyInfoTelShow"]/span[2])').extract()
            item2['contactsnumber'] = item2['contactsnumber'][0] if len(item2['contactsnumber']) > 0 else ''

            yield item2

