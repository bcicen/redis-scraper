#!/usr/bin/python

import os,redis,json,logging,time
from string import digits

log = logging.getLogger()

class ProcessRedisQ(object):
    def __init__(self,redis_pool,log_dir,redis_port=6379):
        self.r_hosts = redis_pool
        self.r_port  = redis_port
        self.log_dir = log_dir
        self.poll()    

    def poll(self):
        for h in self.r_hosts:
            self.process(h)

    def process(self, host):
        stime = time.time()
        r = redis.StrictRedis(host=host,port=self.r_port,db=0)
        log.debug('connected to redis host at %s:%s' % (host,str(self.r_port)))
        kcount = 0
        for k in [ k for k in r.keys() if r.type(k) == 'list' ]:
            wcount = 0
            klen = r.llen(k)
            f = "" + self.log_dir + "/" + k + ".log"
            of = open(f, 'a')
            #pop to process queue and write to file
            log.debug('reading %s values from key %s' % (str(klen),str(k)))
            for l in range(0, klen):
                logline = r.rpoplpush(k, 'processing')
                of.write(k + ":" + logline + '\n')
                wcount += 1
                if wcount % 100 == 0:
                    log.debug('wrote 100 lines to file')
            of.close()
            #
            if wcount == klen:
                r.delete('processing')
                kcount += wcount
            else:
                raise Exception('proccesing queue and list are not balanced, aborting!')

        if kcount != 0:
            log.info('%s: processed %s entries to file in %s seconds' % (
                time.strftime("%d-%b-%Y %H:%M:%S", time.localtime()),
                kcount,
                (time.time() - stime)
                ))
        else:
            log.info('no lists found to process')
