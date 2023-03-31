from pathlib import Path

BOT_NAME = 'pep_parse'
SPIDER_MODULES = ['pep_parse.spiders']
# NEWSPIDER_MODULE = 'pep_parse.spiders'
ROBOTSTXT_OBEY = True

BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = 'results'

ALLOWED_DOMAINS = 'peps.python.org'
START_URLS = 'https://peps.python.org/'

ITEM_PIPELINES = {'pep_parse.pipelines.PepParsePipeline': 300}

FEEDS = {
    f'{RESULTS_DIR}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
    },
}
