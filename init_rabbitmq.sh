#!/bin/bash
set -e

# 等待rabbitmq-server ready
rabbitmq_count=`docker ps | grep rabbitmq | grep -v grep | wc -l`
while [ $rabbitmq_count -eq 0 ]
do
    sleep 1
    echo 'waiting...'
done

# 创建 vhost
docker exec rabbitmq rabbitmqctl add_vhost celery_demo
# 创建 user
docker exec rabbitmq rabbitmqctl add_user testonly testonly
# 给创建的 user 赋予权限
docker exec rabbitmq rabbitmqctl set_permissions -p celery_demo testonly ".*" ".*" ".*"
