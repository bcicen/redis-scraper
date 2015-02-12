#!/usr/bin/python

import os,sys,logging
from argparse import ArgumentParser
from .core import ProcessRedisQ
from . import __version__

log = logging.getLogger()
logging.basicConfig(level=logging.INFO)

def main():
    parser = ArgumentParser(description='read logs from redis queue to a directory')
    parser.add_argument('-v', action='version', version=__version__)
    parser.add_argument('-r', dest='redispool', type=str, action='append', 
            help='redis db to poll. can be specified multiple times')
    parser.add_argument('-p', dest='redisport', type=int, default=6379, 
            help='port to reach redis host(s) on')
    parser.add_argument('-d', dest='logdir', help='path of directory to log to',
            default='/etc/tsmutils/tags.yaml')

    args = parser.parse_args()

    if not args.redispool:
        print('you must specify at least one redis host')
        sys.exit(0)

    if not args.logdir:
        print('you must specify a logdir')
        sys.exit(0)

    try:
        test = open("" + args.logdir + ".testfile", 'a')
        test.close()
    except IOError as e:
        raise Exception(e)

    #run
    ProcessRedisQ(args.redispool,args.logdir,redis_port=args.redisport, interval=10)

if __name__ == '__main__':
    main()
