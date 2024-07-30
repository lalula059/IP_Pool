from logger.log import logger
from data_redis import Data_Redis
from config import headers_list
import requests
import random
import asyncio
import aiohttp
# proxy = {
#     'http' : 'http://114.106.172.163:8089',
#     'https' : 'http://114.106.172.163:8089'
# }
# headers = {
#                        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
#                        "Connection": "close"}

# resp = requests.get(url = 'https://httpbin.org/get',headers=headers,proxies=proxy,verify=False)
# print(resp.text)
class Examine:
    def __init__(self) -> None:
        self.redis = Data_Redis()
        self.event_loop = asyncio.get_event_loop()
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    async def check_ip(self,ip,score,session,sem):
        try:
            async with sem:
                logger.info(f'正在检测代理{ip}发送请求是否可用')
                async with session.get(url='https://httpbin.org/get',headers=random.choice(headers_list),proxy='http://'+ip) as resp:
                    res = await resp.json()
                    logger.info("成功一次了{}".format(res))
                    if res['origin']:
                        self.redis.max(ip)
        except Exception as e:
            if score <=70:
                self.redis.remove(ip)
            else:
                self.redis.update(ip,score)
            logger.error(f'此链接不可用{e}')



    async def get_from_database(self):
        try:
            item = self.redis.get_ip()
            logger.info("正在从redis库里面得到ip")
            return item
        except Exception as e:
            logger.error("池里面没有ip了")

    async def main(self):
        items = await self.get_from_database()
        session = aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(10),connector=aiohttp.TCPConnector(verify_ssl=False))
        sem = asyncio.Semaphore(5)
        tasks = [asyncio.create_task(self.check_ip(item[0].decode('utf-8'),item[1],session,sem)) for item in items]
        await asyncio.gather(*tasks)
        session.close()
    def start(self):
            self.event_loop.run_until_complete(self.main())
    