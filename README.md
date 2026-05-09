# Ransomware-Resilient Backup & Recovery Platform

Production-focused international-hackathon project implementing resilient backup orchestration, immutable vaulting, dependency-aware recovery, ransomware simulation, and SOC-grade operations dashboards.

## Folder Structure

- `backend/` FastAPI, async services, Celery worker, API modules, database models/migrations, tests
- `frontend/` Next.js TypeScript dashboard, cybersecurity dark-theme pages, charts, topology views
- `infra/monitoring/` Prometheus and Grafana provisioning
- `infra/k8s/` Kubernetes deployment example
- `scripts/` startup automation
- `docs/` architecture, security, playbooks, setup and deployment guides

## Quick Start

```bash
cp backend/.env.example backend/.env
./scripts/bootstrap.sh
```

Services:
- Backend API: `http://localhost:8000/docs`
- Frontend: `http://localhost:3000`
- Prometheus: `http://localhost:9090`
- Grafana: `http://localhost:3001`

## Core Modules

1. Backup Orchestration Engine (full/incremental backups, version catalog)
2. Immutable Backup Vault (object lock + retention)
3. Backup Integrity Verification (checksums + scheduled checks)
4. Recovery Orchestrator (dependency-aware restore ordering)
5. Ransomware Detection Simulator (safe attack replay)
6. Infrastructure Dependency Mapper (graph restore planner)
7. Incident Dashboard (live monitoring + telemetry)
8. Zero Trust Access (JWT + RBAC + audit trail)
9. Recovery Drill Engine (Celery scheduled drills)
10. Analytics & Reporting (readiness, MTTR, risk scores)

## Security

- JWT auth with RBAC authorization guard
- Encryption helper module for protected payload handling
- Immutable backup retention semantics in vault service
- Audit log persistence for privileged actions
- Containerized secrets via env vars

## Testing

```bash
PYTHONPATH=backend pytest -q backend/tests
```

## Documentation

See `docs/` for architecture diagrams, API map, deployment and incident playbooks.
