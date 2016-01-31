# -*- coding: utf-8 -*-

# Scrapy settings for wallPaper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'wallPaper'

SPIDER_MODULES = ['wallPaper.spiders']
NEWSPIDER_MODULE = 'wallPaper.spiders'


ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}
IMAGES_STORE = '../pic'
IMAGE_EXPIRES = 15
