#!/bin/bash
# Assign arguments
target_app_amount=$1

# Start Rest API Server
if (( $(docker ps -f name=rest-api-server | wc -l) < 2 ))
then
    docker run -d --name rest-api-server -p 80:80 -v /var/run/docker.sock:/tmp/docker.sock:ro jwilder/nginx-proxy
fi

# Start/stop REST API Apps
app_amount=$(( $(docker ps -f ancestor=rest-api-app | wc -l) - 1 ))
if (( app_amount < target_app_amount ))
then
    for (( i = 0; i < target_app_amount-app_amount; i++ ))
    do
    docker run -v `pwd`/db:/db -d -e VIRTUAL_HOST=domain.local rest-api-app
    done
elif (( app_amount > target_app_amount ))
then
    docker ps | awk '{ print $1,$2 }' | grep rest-api-app | awk '{print $1 }' | head -n $(( app_amount - target_app_amount )) | xargs -I {} docker rm -f {}
fi

# Perform database cleanup
if (( target_app_amount > 0 ))
then
    curl -s http://localhost/cleanup/
fi