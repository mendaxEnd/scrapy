from scrapy import spiders
from scrapy.selector import Selector
from wallPaper.items import WallpaperItem

class WallpaperSpider(spiders.Spider):
    name = "wallpaper"
    allowed_domains = ["cn.forwallpaper.com"]
    start_urls = ["http://cn.forwallpaper.com/images/photography.html"]

    def parse(self, response):
        item = WallpaperItem()
        sel = Selector(response)
        item['image_urls'] = sel.xpath('//img/@src').extract()
        item['images'] = sel.xpath('//img/@src').re(r'[^/]*.jpg$')
        return item
