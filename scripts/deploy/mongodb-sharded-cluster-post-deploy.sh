#!/usr/bin/env bash

set -x #echo on

# Post deploy script for mongodb-sharded-cluster

kubectl exec mongodb-sharded-cluster-statefulset-0 -it -- bash -c "mongosh \
    admin \
    -u \${MONGO_INITDB_ROOT_USERNAME} \
    -p \${MONGO_INITDB_ROOT_PASSWORD}" \
    < ./scripts/deploy/mongodb-sharded-cluster-replica-set-initiate.js

echo done
