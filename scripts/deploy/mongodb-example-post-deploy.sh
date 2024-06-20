#!/usr/bin/env bash

set -x #echo on

# Post deploy script for mongodb-example

kubectl exec mongodb-example-statefulset-0 -it -- mongosh < ./scripts/deploy/mongodb-example-post-deploy.js
echo done
