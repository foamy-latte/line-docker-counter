#!/bin/bash
docker build --file ./rest-api-app/Test.Dockerfile --tag rest-api-app-test ./rest-api-app
docker run -v `pwd`/db:/db rest-api-app-test