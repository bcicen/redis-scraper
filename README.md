# redis-scraper

redis-scraper is a small program that utilizes a reliable queue pattern to simply pull the contents of all queues/keys in a given redis instance to a flat file periodically.

## Quickstart

The easiest way to use redis-scraper is by running the dockerhub image in a container locally, with a space-separated list of redis hosts as an argument:
```
docker run -d -v $(pwd):/data bcicen/redis-scraper redishost1.mydomain redishost2.mydomain
```
Or building the image yourself:
```
git clone https://github.com/bcicen/redis-scraper.git
cd redis-scraper
docker build -t redis-scraper .
docker run -d -v $(pwd):/data redis-scraper redishost1.mydomain redishost2.mydomain
```
redis-scraper will start pulling all keys stored in redis to respective files in the directory mounted at /data, polling every 60s. 

## CLI Usage

```
redis-scraper -r 127.0.0.1 -p 6379 -d /var/log/redis-dumps/
```


```
  -r REDISPOOL  redis db to poll. can be specified multiple times
  -p REDISPORT  port to reach redis host(s) on
  -d LOGDIR     path of directory to log to
```
