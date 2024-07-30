import re
import requests
import json
from crawler.base_fetch import Base_Fetch
from config import NUMBERS,MIN_NUMBERS
from logger.log import logger
from proxy.proxy import Proxy
from data_redis import Data_Redis
url_main = 'https://www.kuaidaili.com/free/inha/{}'



class kuaidaili(Base_Fetch):
    
    
    def __init__(self) -> None:
        super().__init__()
        self.urls = [url_main.format(i) for i in range(MIN_NUMBERS,NUMBERS)]
        self.redis = Data_Redis()
        # self.value = None
    def produce_ip(self):
        for ip_host in self.value:
            logger.info(f"迭代代理中{ip_host}")
            yield Proxy(host=ip_host.get('ip'),port = ip_host.get('port'))


    def parse(self,html):
        try:
            pattern = re.compile('fpsList.*?(\[\{.*);')
            value = json.loads(pattern.findall(html)[0])
            self.value = value
            for item in self.produce_ip():
                logger.info(item)
                self.redis.insert_ip_host(item)
                logger.info("插入IP中{}".format(item))
        except Exception as e:
            logger.error(f"解析并插入数据中出现错误{e}")