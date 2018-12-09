#!/bin/bash
docker build --file ./rest-api-app/TestNoCoverage.Dockerfile --tag rest-api-app-test-no-coverage ./rest-api-app
docker run -v `pwd`/db:/db rest-api-app-test-no-coverage