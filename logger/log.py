import logging
from config import ROOT_LOG
import os
def check_filename():
    if not os.path.exists(ROOT_LOG):
        file = open(ROOT_LOG,'w')
        file.close()
def getlogger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    if not logger.hasHandlers():
        stream_handler = logging.StreamHandler()
        File_handler = logging.FileHandler(filename=ROOT_LOG)
        format_console = logging.Formatter("%(levelname)s--[[%(module)s.py---%(lineno)d]]----%(asctime)s::::::%(message)s")
        stream_handler.setFormatter(format_console)
        File_handler.setFormatter(format_console)
        logger.addHandler(stream_handler)
        logger.addHandler(File_handler)
    return logger
logger = getlogger()
