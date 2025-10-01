from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt

# ===== Configurações =====
SECRET_KEY = "SEU_SEGREDO_AQUI"  # futuramente, use variáveis de ambiente
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# ===== Contexto para bcrypt =====
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ===== Funções de Senha =====
def hash_password(password: str) -> str:
    # Garante que seja string
    if not isinstance(password, str):
        password = str(password)
    # Corta a senha para 72 bytes (limite do bcrypt)
    password_bytes = password.encode("utf-8")[:72]
    password_truncated = password_bytes.decode("utf-8", "ignore")
    return pwd_context.hash(password_truncated)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# ===== Funções JWT =====
def create_access_token(data: dict, expires_delta: int = ACCESS_TOKEN_EXPIRE_MINUTES):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
