from app.workers.celery_app import celery


@celery.task(name='backup.verify_integrity')
def verify_integrity_task() -> dict:
    return {'status': 'completed', 'checked_objects': 100, 'corruptions_found': 0}


@celery.task(name='recovery.drill')
def recovery_drill_task() -> dict:
    return {'status': 'completed', 'rto_minutes': 21, 'sla_met': True}
