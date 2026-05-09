# Deployment Guide

## Docker Compose

- Productionize by pinning image tags, enabling TLS ingress, and managed Postgres/Redis.

## Kubernetes

- Use `infra/k8s/backend-deployment.yaml` as baseline.
- Add ingress + cert-manager + sealed secrets in production.
