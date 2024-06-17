SHELL:=/usr/bin/env bash -O globstar

# linters
shellcheck:
	shellcheck tests/infra/tests/*.sh

yamllint:
	yamllint -c .yamllint.yaml .

kube-linter:
	kube-linter lint k8s

lint: yamllint shellcheck kube-linter

# cluster
start-cluster:
	minikube start \
		--driver=docker \
		--addons=ingress \
		--addons=ingress-dns \
		--addons=metrics-server \
		--insecure-registry="host.minikube.internal:5000" \
		--nodes 2

stop-cluster:
	minikube stop

delete-cluster:
	minikube delete

show-local-domains:
	sudo $(shell which python) scripts/update_domains.py show

update-local-domains:
	sudo $(shell which python) scripts/update_domains.py update $(shell minikube ip)

minikube-ssh:
	minikube ssh

minikube-dashboard:
	minikube dashboard

show-endpoints:
	minikube ip

# registry
show-proccess-on-port-5000:
	sudo lsof -i :5000

start-registry:
	sudo systemctl stop docker-registry || true
	docker compose -f docker-compose.registry.yaml up -d

stop-registry:
	docker compose -f docker-compose.registry.yaml down

delete-registry:
	docker compose -f docker-compose.registry.yaml down --rmi local --volumes

# images
build-images:
	docker compose build

remove-images:
	docker compose down --rmi local

show-images:
	docker images | grep k8s-sandbox- || true

push-images:
	bash scripts/push-images.sh

show-registry-images:
	curl -s -X GET http://host.minikube.internal:5000/v2/_catalog | jq --color-output .

# k8s
k8s-apply:
	kubectl apply -f k8s/volumes
	kubectl apply -f k8s/storage
	kubectl apply -f k8s/configs
	kubectl apply -f k8s/db
	kubectl apply -f k8s/services

k8s-delete:
	kubectl delete -f k8s/services || true
	kubectl delete -f k8s/db || true
	kubectl delete -f k8s/configs || true

k8s-delete-all:
	kubectl delete -f k8s/services || true
	kubectl delete -f k8s/db || true
	kubectl delete -f k8s/configs || true
	kubectl delete -f k8s/storage || true
	kubectl delete -f k8s/volumes || true

show-nodes:
	kubectl get nodes

restart-deployments:
	kubectl rollout restart deployment

show-deployments:
	kubectl get deployments

show-replicas:
	kubectl get replicasets

show-pods:
	kubectl get pods

show-services:
	kubectl get services

show-ingresses:
	kubectl get ingresses

show-namespaces:
	kubectl get namespaces

show-all:
	kubectl get all

# deploy
deploy: build-images push-images k8s-apply restart-deployments

# packages lint
lint-k8s-sandbox-activity:
	docker compose run --build --rm activity-python
	docker compose run --build --rm activity-typescript

# tests
test-tests-infra:
	docker compose run --build --rm tests-infra

test-tests-integration:
	docker compose run --build --rm tests-integration

test: test-tests-infra test-tests-integration
