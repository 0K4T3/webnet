import argparse
import sys
from typing import List

from webnet.commands import StartCommand


argparser = argparse.ArgumentParser()
subparsers = argparser.add_subparsers()

subparser_start = subparsers.add_parser('start', help='')
subparser_start.add_argument('-p', '--port', required=False, default=6789, type=int)
subparser_start.set_defaults(handler=lambda args: StartCommand().process(args.port))


def main(args: List[str] = sys.argv):
    _, *args = args
    parsed_args = argparser.parse_args()
    parsed_args.handler(parsed_args)
