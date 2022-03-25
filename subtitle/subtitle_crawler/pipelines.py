# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SubtitleCrawlerPipeline(object):
    def process_item(self, item, spider):
        url = item['url']
        file_name = url.replace('/','_').replace(':','_')
        with open(f'result/{file_name}', 'w') as fp:
            fp.write(item['body'])
        return item

