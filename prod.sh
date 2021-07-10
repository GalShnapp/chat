#!/bin/bash


SERVER_IP


dockers=($(docker ps | awk  '$1~/[a-z1-9]/ {printf "%s,%s", $1, $4}'))
clients=($(echo "${dockers[*]}" | awk -F"," '$2~/client/ {print $1}'))
servers=($(echo "${dockers[*]}" | awk -F"," '$2~/server/ {print $1}'))

for server in ${servers[*]};
do
	server_ip=$(docker inspect $server | grep "IPAdd" | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | tr ' ' '\n' | uniq)
	echo $server_ip
	SERVER_IP=$server_ip
done

for doc in ${servers[*]};
do
	echo "$doc"
done


for doc in ${clients[*]};
do
        echo "$doc"
done


