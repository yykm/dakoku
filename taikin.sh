#!/bin/sh

cd `dirname $0`

docker-compose up -d
sleep 3
docker-compose exec app python ./src/dakoku_taikin.py

docker-compose down