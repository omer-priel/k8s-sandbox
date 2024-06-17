# K8s sandbox

## Table of Contents

* [Roadmap / Tasks](#roadmap--tasks)
* [Tecnologies](#tecnologies)
* [Requirements](#requirements)
* [Installation](#installation)
* [Data Flow](#data-flow)
* [File Structure](#file-structure)
* [License](#license)

## Roadmap / Tasks

* services
  * Go
    * http rest server
    * Gin
  * Python
    * FastAPI
    * Flask
  * JavaScript:
    * Express
    * Fastify


* test
  * curl / bash
  * go test
  * pytest
  * jest

* service level
  * schemas
  * fake data models
  * routes
  * entry points
  * static configs

* Databases / Entities Storage
  * PostgresSQL
  * MySQL
  * MongoDB
  * Redis
  * JSON
  * XML
  * CSV

* service level 2
  * connectors

* packages
  * schema packages
  * connectors packages 
  * entities packages
  * named queries packages

* clients (desktop)
  * cli - go

* services
  * Django - Python
  * NestJS - TypeScript

* static
  * react (vite + TypeScript)
  * Vanilla JS (HTML + CSS + JS)
  * Vanilla TS (HTML + CSS + TS)
  * Vue
  * SolidJS
  * Angular
  * Svelte

* packages
  * api sdks (controllers)
    * JavaScript
    * TypeScript
    * Python
    * Go

* services
  * NextJS - TypeScript

coming soon

## Tecnologies

* Docker
* Docker Compose
* Kubernetes
* minikube
* yamllint
* shellcheck

## Requirements

* qemu
* minikube
* Docker
* kubectl
* resolvconf
* yamllint
* go
* kube-linter
* shellcheck

## Installation

1. Run the following command for edit the file `/etc/hosts`:

```bash
sudo nano /etc/hosts
```

Add the following line:

```txt
127.0.0.1  host.minikube.internal
```

## Data Flow

Current On local machine:

```mermaid
flowchart LR
  subgraph docker-hub
    nginx-base-image
    node-base-image
    python-base-image
    go-base-image
  end
  subgraph Docker Host Containers
    subgraph local-registy
      nginx-image
      express-image
      fastapi-image
      flask-image
      fastify-image
      gohttp-image
      gin-image
    end
    subgraph cluster[cluster minikube]
      subgraph control-plane-node
        k8s-api-server
        s8s-scheduler
        controller-manager
        etcd

        nginx-pod-1
        express-pod-1
        fastapi-pod-1
        flask-pod-1
        fastify-pod-1
        gohttp-pod-1
        gin-pod-1
      end

      subgraph worker-node
        nginx-pod-2
        nginx-pod-3
        express-pod-2
        express-pod-3
        fastapi-pod-2
        fastapi-pod-3
        flask-pod-2
        flask-pod-3
        fastify-pod-2
        fastify-pod-3
        gohttp-pod-2
        gohttp-pod-3
        gin-pod-2
        gin-pod-3
      end
      
      worker-node <---> control-plane-node

      nginx-image --> nginx-deployment
      nginx-deployment --> nginx-pod-1 & nginx-pod-2 & nginx-pod-3

      express-image --> express-deployment
      express-deployment --> express-pod-1 & express-pod-2 & express-pod-3

      fastapi-image --> fastapi-deployment
      fastapi-deployment --> fastapi-pod-1 & fastapi-pod-2 & fastapi-pod-3

      flask-image --> flask-deployment
      flask-deployment --> flask-pod-1 & flask-pod-2 & flask-pod-3

      fastify-image --> fastify-deployment
      fastify-deployment --> fastify-pod-1 & fastify-pod-2 & fastify-pod-3
      
      gohttp-image --> gohttp-deployment
      gohttp-deployment --> gohttp-pod-1 & gohttp-pod-2 & gohttp-pod-3

      gin-image --> gin-deployment
      gin-deployment --> gin-pod-1 & gin-pod-2 & gin-pod-3

      nginx-service --> nginx-pod-1 & nginx-pod-2 & nginx-pod-3
      express-service --> express-pod-1 & express-pod-2 & express-pod-3
      fastapi-service --> fastapi-pod-1 & fastapi-pod-2 & fastapi-pod-3
      flask-service --> flask-pod-1 & flask-pod-2 & flask-pod-3
      fastify-service --> fastify-pod-1 & fastify-pod-2 & fastify-pod-3
      gohttp-service --> gohttp-pod-1 & gohttp-pod-2 & gohttp-pod-3
      gin-service --> gin-pod-1 & gin-pod-2 & gin-pod-3
      
      nginx-ingress --> nginx-service
      express-ingress --> express-service
      fastapi-ingress --> fastapi-service
      flask-ingress --> flask-service
      fastify-ingress --> fastify-service
      gohttp-ingress --> gohttp-service
      gin-ingress --> gin-service
    end
  end
  subgraph Maintainer
    subgraph CI
      pull-nginx[pull] --> nginx-base-image
      pull-nginx --> build-nginx[build] --> nginx-image
      
      pull-express[pull] --> node-base-image
      pull-express --> express-nginx[build] --> lint-express[lint] --> express-image
      
      pull-fastapi[pull] --> python-base-image
      pull-fastapi --> fastapi-nginx[build] --> fastapi-image
      
      pull-flask[pull] --> python-base-image
      pull-flask --> flask-nginx[build] --> flask-image
      
      pull-fastify[pull] --> node-base-image
      pull-fastify --> fastify-nginx[build] --> lint-fastify[lint] --> fastify-image

      pull-gohttp[pull] --> go-base-image
      pull-gohttp --> gohttp-nginx[build] --> gohttp-image

      pull-gin[pull] --> go-base-image
      pull-gin --> gin-nginx[build] --> gin-image
    end

    Terminal-Maintainer[Terminal] ---> local-registy
    Terminal-Maintainer --> CI
    Terminal-Maintainer --> kubectl --> k8s-api-server
    Terminal-Maintainer ---> nginx-ingress & express-ingress & fastapi-ingress & flask-ingress & fastify-ingress & gohttp-ingress & gin-ingress
    Browser-Maintainer[Browser] ---> nginx-ingress & express-ingress & fastapi-ingress & flask-ingress & fastify-ingress & gohttp-ingress & gin-ingress
  end
  subgraph Client
    Browser ---> nginx-ingress & express-ingress & fastapi-ingress & flask-ingress & fastify-ingress & gohttp-ingress & gin-ingress
  end
```

Full Target:

```mermaid
flowchart LR
  subgraph Cluster
    subgraph Master
      K8s-API-Server
      K8s-Scheduler
      Controller-Manager
      etcd
    end

    subgraph Node1 [Node 1]
      API-1
      Redis-1
    end
    subgraph Node2 [Node 2]
      API-2
      Redis-2
    end
    
    Node1 & Node2 <---> Master

    API-service --> API-1 & API-2
    Redis-service --> Redis-1 & Redis-2
    API-Ingress --> API-service
    Redis-Ingress --> Redis-service
  end
  subgraph Maintainer
    Terminal-Maintainer[Terminal] --> kubectl --> K8s-API-Server
    Terminal-Maintainer  ---> Redis-Ingress
    Browser-Maintainer[Browser] ---> API-Ingress
  end
  subgraph Client
    Browser ---> API-Ingress
    Terminal --> CLI --> API-Ingress
  end
```

## File Structure

k8s-sandbox
* clients
  * cli
* k8s
* packages
* scripts
* services
* tests
 * infra
 * integration

## License

MIT
