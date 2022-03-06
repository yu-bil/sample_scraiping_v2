# -*- coding: utf-8 -*-
import scrapy

from ..selenium_middleware import close_driver


class SomeSpider(scrapy.Spider):
    name = "some_spider"
    allowed_domains = ["somedomain"]
    start_urls = (
        'http://somedomain/',
    )
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            "some_crawler.selenium_middleware.SeleniumMiddleware": 0,
        },
        "DOWNLOAD_DELAY": 0.5,
    }


    def parse(self, response):
        # クローラーの処理

    def closed(self, reason):
        close_driver()
