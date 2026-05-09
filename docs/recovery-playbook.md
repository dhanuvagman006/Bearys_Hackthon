# Recovery Playbook

1. Validate incident scope in dashboard.
2. Lock latest clean backups in immutable vault.
3. Trigger dependency-aware recovery plan.
4. Execute staged restore (critical-first).
5. Verify service health and rollback on failures.
6. Publish MTTR/report metrics for post-incident review.
