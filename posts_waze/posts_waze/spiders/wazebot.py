# -*- coding: utf-8 -*-
import scrapy


class WazebotSpider(scrapy.Spider):
    name = 'wazebot'
    allowed_domains = ['https://play.google.com/store/apps/details?id=com.waze']
    start_urls = ['https://play.google.com/store/apps/details?id=com.waze&hl=pt_BR']


    def parse(self, response):
	

	titles = response.css(".review-body.with-review-wrapper::text").extract()

	for item in zip(titles):
            	scraped_info = {
       	        	'title' : item[0]
       	    	}

		yield scraped_info	


        
