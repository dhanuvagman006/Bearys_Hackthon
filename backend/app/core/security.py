from datetime import datetime, timedelta, timezone
from hashlib import sha256
from jose import jwt
from passlib.context import CryptContext
from cryptography.fernet import Fernet

from app.core.config import settings

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


def create_access_token(subject: str, role: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)
    payload = {'sub': subject, 'role': role, 'exp': expire}
    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)


def encrypt_payload(data: bytes) -> bytes:
    return Fernet(settings.encryption_key.encode()).encrypt(data)


def decrypt_payload(data: bytes) -> bytes:
    return Fernet(settings.encryption_key.encode()).decrypt(data)


def checksum(data: bytes) -> str:
    return sha256(data).hexdigest()
