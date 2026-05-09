#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."
docker compose up -d --build
sleep 5
docker compose exec backend alembic upgrade head
