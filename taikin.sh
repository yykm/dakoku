#!/bin/sh

cd `dirname $0`

docker-compose up -d

# スリープ挟まないとコネクション確率前にコマンド実行してしまう
sleep 3
docker-compose run -T app bash -c './jpholidayp/jpholidayp || python ./src/dakoku_taikin.py'

docker-compose down