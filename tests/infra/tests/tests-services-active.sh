#!/usr/bin/env bash

set -x #echo on

curl -X GET http://tests-private.test/ 2> /dev/null | jq --color-output ".service" | grep tests-private || exit 1
