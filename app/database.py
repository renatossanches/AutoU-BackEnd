import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ===== Variáveis de ambiente =====
DATABASE_URL = os.environ.get("DATABASE_URL")  # Definida no Railway

# ===== Configuração SQLAlchemy =====
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ===== Função para criar banco =====
def init_db():
    from app.models import User, Email  # importa os modelos
    Base.metadata.create_all(bind=engine)

# ===== Dependency para rotas =====
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
