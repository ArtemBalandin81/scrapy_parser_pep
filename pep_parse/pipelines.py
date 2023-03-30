from collections import defaultdict
from datetime import datetime

from .constants import BASE_DIR, RESULTS_DIR

DATE_FORMAT = '%Y-%m-%d_%H-%M-%S'
SPIDER_STATUS_NAME = (
    f'status_summary_{datetime.now().strftime(DATE_FORMAT)}.csv'
)


class PepParsePipeline:

    def open_spider(self, spider):
        self.total_status = defaultdict(int)
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        self.total_status[item['status']] += 1
        return item

    def close_spider(self, spider):

        with open(
                f'{self.results_dir}/{SPIDER_STATUS_NAME}',
                mode='w',
                encoding='utf-8'
        ) as f:
            f.write('Status,Quantities\n')
            for status, quantity in self.total_status.items():
                f.write(f'{status},{quantity}\n')
            f.write(f'Total,{sum(self.total_status.values())}\n')
