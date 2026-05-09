from app.services.analytics_service import compute_readiness_score


def test_readiness_score_in_range():
    score = compute_readiness_score(0.9, 60, 0.8)
    assert 0 <= score <= 100
    assert round(score, 2) == score
