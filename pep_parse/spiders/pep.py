import re
from urllib.parse import urljoin

import scrapy

from ..items import PepParseItem
from ..settings import ALLOWED_DOMAINS, START_URLS


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [ALLOWED_DOMAINS]
    start_urls = [START_URLS]

    def parse(self, response):
        """Находит все ссылки на pep."""
        all_peps = response.css(
            '#numerical-index tbody tr a::attr(href)'
        ).getall()
        for pep_link in all_peps:
            yield response.follow(
                urljoin(
                    START_URLS,
                    pep_link
                ),
                callback=self.parse_pep
            )

    def parse_pep(self, response):
        """Парсит страницы отдельных pep."""
        page_title = response.css('#pep-content h1::text').get()
        pattern_name = r'\– (.*)'
        data = {
            'number': page_title.split()[1],
            'name': re.search(pattern_name, page_title)[1],
            'status': response.css(
                '#pep-content h1 + dl dd.field-even abbr::text'
            ).get()
        }
        yield PepParseItem(data)
