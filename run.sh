#!/bin/bash

DATADIR="/data"
REDIS_POOL=$@

[ -z "$REDIS_POOL" ] && {
  echo "At least one redis host must be provided"
  exit 1 
}

[ ! -d "$DATADIR" ] && {
  echo "No volume mounted at $DATADIR"
  exit 1 
}

[ -z "$REDIS_PORT" ] && {
    REDIS_PORT=6379
}

echo "Starting redis-scraper, writing to $DATADIR"
redis-scraper $(for r in $REDIS_POOL; do echo -n "-r $r "; done) -p $REDIS_PORT -d $DATADIR
