def compute_readiness_score(backup_success_rate: float, avg_recovery_minutes: int, verification_coverage: float) -> float:
    score = (backup_success_rate * 0.4) + ((1 - min(avg_recovery_minutes / 180, 1)) * 0.3) + (verification_coverage * 0.3)
    return round(max(0.0, min(score, 1.0)) * 100, 2)
