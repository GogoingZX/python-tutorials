import sys
import os
import re
import json
import time
import datetime
import pickle
import logging

#---------------------------------------------------------------------------------------------------
TODAY = datetime.datetime.today()
TODAY_STRING = TODAY.strftime(r"%Y-%m-%d")
TODAY_STRING_YMD = TODAY.strftime(r"%Y%m%d")


if __name__ == "__main__":
    execution_folder = os.path.abspath(os.path.dirname(__file__))
    execution_file = os.path.basename(os.path.abspath(__file__))
    filename = execution_file[::-1].split(".", 1)[1][::-1] # to avoid the edge case with multiple dots

    log_folder = os.path.join(execution_folder, "log")
    if not os.path.exists(log_folder):
        os.mkdir(log_folder)

    logging.basicConfig(
        filename=os.path.join(log_folder, f"{TODAY_STRING_YMD}_{filename}.log"),
        filemode="w",
        encoding="utf-8",
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] <%(name)s> %(lineno)s: %(message)s",
            # https://docs.python.org/3/library/logging.html#logrecord-attributes
        datefmt=r"%m-%d %H:%M:%S"
            # https://docs.python.org/3/library/time.html#time.strftime
    )

    logger = logging.getLogger(__name__)

    logger.info("Test Info")
    logger.debug("Test Debug")
    logger.debug("Test Warning")