from logger.log import logger
import crawler
import time
from core.check import Examine
from config import CYCLE,LOOP

def getter():
    cout = 0
    while True:
        for cls in crawler.classes:
            """需要实例化，因为你的列表url是实例化才有的"""
            cls().crawl()
        logger.info("正在等待进行下一个getter循环")
        cout+=1
        time.sleep(CYCLE)
        if cout == LOOP:
            return

def examiner():
    cout = 0
    while True:
        check = Examine()
        check.start()
        logger.info("正在等待进行下一个examiner循环")
        time.sleep(CYCLE)
        cout+=1
        time.sleep(CYCLE)
        if cout == LOOP:
            return