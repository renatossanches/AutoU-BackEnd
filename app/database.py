import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

# ===== Variáveis de ambiente =====
DATABASE_URL = os.environ.get("DATABASE_URL")  # Definida no Railway

# ===== Configuração SQLAlchemy =====
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,      # verifica a conexão antes de usar
    pool_size=10,            # quantidade de conexões no pool
    max_overflow=20,         # conexões extras além do pool
    pool_recycle=1800        # reinicia conexão após 30 min (em segundos)
)
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
    except OperationalError:
        db.close()
        db = SessionLocal()
        yield db
    finally:
        db.close()
