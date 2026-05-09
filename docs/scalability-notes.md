# Scalability Notes

- Horizontal API scaling via stateless FastAPI pods.
- Celery worker pools for parallel verification/recovery jobs.
- PostgreSQL indexing and partitioning for large backup catalogs.
- Redis queue sharding for high-volume drill workloads.
