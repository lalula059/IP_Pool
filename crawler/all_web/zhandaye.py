# import re
# import requests
# import json
# from crawler.base_fetch import Base_Fetch
# from config import NUMBERS,MIN_NUMBERS
# from logger.log import logger
# from proxy.proxy import Proxy
# from data_redis import Data_Redis
# url_main = 'https://www.zdaye.com/free/{}'



# class zhangdaye(Base_Fetch):
    
    
#     def __init__(self) -> None:
#         super().__init__()
#         self.urls = [url_main.format(i) for i in range(MIN_NUMBERS,NUMBERS)]
#         self.redis = Data_Redis()
#         # self.value = None
#     def produce_ip(self):
#         for item in self.value:
#             ip = self.value.xpath('/td[1]//text()').getall()
#             port = self.value.xpath('./td[2]//text()').getall()
#             logger.info(f"迭代代理中{ip+":"+port}")
#             yield Proxy(host=ip,port = port)


#     def parse(self,html):
#         try:
#             self.se_an = self.selector(html)
#             self.value = self.se_an.xpath('//tr')
#             for item in self.produce_ip():
#                 logger.info(item)
#                 self.redis.insert_ip_host(item)
#                 logger.info("插入IP中{}".format(item))
#         except Exception as e:
#             logger.error(f"解析并插入数据中出现错误{e}")



# from parsel import Selector
# headers = {
#                        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
#                        "Connection": "close"}

# resp = requests.get(url = 'https://www.zdaye.com/free/1',headers=headers)
# print(resp.status_code)
# se = Selector(resp.text)

# value = se.xpath('//tr')
# for item in value:
#     print(item)
#     ip = value.xpath('/td[1]//text()').getall()
#     host = value.xpath('./td[2]//text()').getall()
#     print(ip)