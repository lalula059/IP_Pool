import requests
from config import headers_list
from logger.log import logger
import random
from  parsel import Selector
import time
WRONG_ERROR = (requests.exceptions.ConnectionError,requests.exceptions.ProxyError)

class Base_Fetch:
    def __init__(self) -> None:
        self.selector = Selector
    def crawl(self):
        for url in self.urls:
            try:
                time.sleep(10)
                html_pre = requests.get(url=url,headers=random.choice(headers_list))
                logger.info('正在请求页面{}'.format(url))
                if html_pre.status_code == 200:
                    html = html_pre.text
                    logger.info('正在解析页面{}'.format(url))
                    self.parse(html)
                else:
                    logger.error(f"出现了网络状态码错误{html_pre.status_code}")
                    logger.error(f'url不可用{url}')
            except WRONG_ERROR as e:
                logger.error(f"出现了网络连接接错误{e}")
            except:
                logger.error(f"出现了未知的错误{e}")