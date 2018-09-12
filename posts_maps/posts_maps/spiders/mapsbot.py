# -*- coding: utf-8 -*-
import scrapy


class WazebotSpider(scrapy.Spider):
    name = 'mapsbot'
    allowed_domains = ['https://play.google.com/store/apps/']
    start_urls = ['https://play.google.com/store/apps/details?id=com.google.android.apps.maps&hl=pt_BR']




    def parse(self, response):
        #Extracting the content using css selectors
        titles = response.css(".review-body.with-review-wrapper::text").extract()
        #Give the extracted content row wise
        for item in zip(titles):
            #create a dictionary to store the scraped info
            scraped_info = {
                'title' : item[0]
            }

            #yield or give the scraped info to scrapy
            yield scraped_info
