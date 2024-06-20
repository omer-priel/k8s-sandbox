#!/usr/bin/env bash

set -x #echo on

# Post deploy script for mongodb-sharded-cluster

kubectl exec mongodb-sharded-cluster-statefulset-0 -it -- mongosh < ./scripts/deploy/mongodb-sharded-cluster-post-deploy.js
echo done
