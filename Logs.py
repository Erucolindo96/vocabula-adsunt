import logging
import argparse

def setLogLevel():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d', '--debug',
        help="Print debugging statements",
        action="store_const", dest="loglevel", const=logging.DEBUG,
        default=logging.WARNING,
        )
    args = parser.parse_args()    
    logging.basicConfig(level=args.loglevel)