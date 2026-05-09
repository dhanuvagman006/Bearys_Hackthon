from app.core.security import checksum


def test_checksum_stable():
    data = b'critical backup payload'
    assert checksum(data) == checksum(data)
