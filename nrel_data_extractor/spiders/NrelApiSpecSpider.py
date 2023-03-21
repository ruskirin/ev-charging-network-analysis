import scrapy
from pathlib import Path


class NrelApiSpecSpider(scrapy.Spider):
    name = 'api_specs'
    start_urls = ['http://developer.nrel.gov/docs/transportation/alt-fuel-stations-v1/all/']
    custom_settings = {
        'FEEDS': {'../data/extractions/data-feature-descriptions1.csv': {'format': 'csv',
                                                                        'overwrite': True}}
    }

    def parse(self, response):
        params = response.xpath(
            '//h2[@id="response-fields"]'
            '/following-sibling::table[@class="doc-parameters"][2]'
            '/tbody'
            '/tr'
        )
        for field in params:
            desc = field.xpath(
                'td[@class="doc-parameter-description"]'
            )
            yield {
                'name': field.xpath(
                    'th[@class="doc-parameter-name"]/text()'
                ).get(),
                'desc_short': desc.xpath(
                    'text()'
                ).get(),
                'desc_long': desc.xpath(
                    'p/text()'
                ).get(),
                'opts': desc.xpath(
                    'table/tbody/tr'
                ).getall()
            }