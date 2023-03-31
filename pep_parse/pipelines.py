import csv
from collections import defaultdict
from datetime import datetime

from .settings import BASE_DIR, RESULTS_DIR

DATE_FORMAT = '%Y-%m-%d_%H-%M-%S'
NAME_FORMAT = 'status_summary_'
TYPE_FILE = '.csv'


class PepParsePipeline:
    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.total_status = defaultdict(int)

    def process_item(self, item, spider):
        self.total_status[item['status']] += 1
        return item

    def close_spider(self, spider):
        with open(
            f'{self.results_dir}/'
            f'{NAME_FORMAT}{datetime.now().strftime(DATE_FORMAT)}{TYPE_FILE}',
            mode='w',
            encoding='utf-8'
        ) as f:
            csv.writer(f, dialect=csv.unix_dialect).writerows(
                [
                    ('Status', 'Quantities'),
                    *self.total_status.items(),
                    ('Total', sum(self.total_status.values()))
                ]
            )
