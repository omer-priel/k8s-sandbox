#!/usr/bin/env bash

set -x #echo on

curl -X GET http://nginx-example.test/index.json 2> /dev/null | jq --color-output ".service" | grep nginx-example || exit 1
curl -X GET http://express-example.test/ 2> /dev/null | jq --color-output ".service" | grep express-example || exit 1
curl -X GET http://fastapi-example.test/ 2> /dev/null | jq --color-output ".service" | grep fastapi-example || exit 1
curl -X GET http://flask-example.test/ 2> /dev/null | jq --color-output ".service" | grep flask-example || exit 1
curl -X GET http://fastify-example.test/ 2> /dev/null | jq --color-output ".service" | grep fastify-example || exit 1
