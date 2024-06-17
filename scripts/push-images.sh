#!/usr/bin/env bash

set -x #echo on

# Push images to local registry

docker tag k8s-sandbox-express-example:latest localhost:5000/k8s-sandbox-express-example:latest
docker push localhost:5000/k8s-sandbox-express-example:latest

docker tag k8s-sandbox-nginx-example:latest localhost:5000/k8s-sandbox-nginx-example:latest
docker push localhost:5000/k8s-sandbox-nginx-example:latest

docker tag k8s-sandbox-fastapi-example:latest localhost:5000/k8s-sandbox-fastapi-example:latest
docker push localhost:5000/k8s-sandbox-fastapi-example:latest

docker tag k8s-sandbox-flask-example:latest localhost:5000/k8s-sandbox-flask-example:latest
docker push localhost:5000/k8s-sandbox-flask-example:latest

docker tag k8s-sandbox-gohttp-example:latest localhost:5000/k8s-sandbox-gohttp-example:latest
docker push localhost:5000/k8s-sandbox-gohttp-example:latest

docker tag k8s-sandbox-gin-example:latest localhost:5000/k8s-sandbox-gin-example:latest
docker push localhost:5000/k8s-sandbox-gin-example:latest
