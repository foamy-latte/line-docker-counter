#!/bin/bash
# Dependencies
apt -y install curl
curl -sSL https://get.docker.com/ | sh

# Compile docker image
docker build --tag rest-api-app ./rest-api-app

# Add execution perms
chmod +x create_counter.sh
chmod +x test.sh
chmod +x test_no_coverage.sh
chmod +x list_counter.sh
chmod +x setup_api.sh
chmod +x wait_counter.sh