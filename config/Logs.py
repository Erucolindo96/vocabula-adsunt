import logging
import argparse

from config import config


def setLogLevel():
    # parser = argparse.ArgumentParser()
    # parser.add_argument(
    #     '-d', '--debug',
    #     help="Print debugging statements",
    #     action="store_const", dest="loglevel", const=logging.DEBUG,
    #     default=logging.INFO,
    #     )
    # args = parser.parse_args()
    # logging.basicConfig(level=args.loglevel)
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=config.logs['level'])
