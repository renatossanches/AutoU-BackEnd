from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers import UserController, EmailController
from app.database import init_db

app = FastAPI(title="AutoU Backend")

# ===== Configuração CORS =====
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===== Inicializa banco =====
init_db()

# ===== Rotas =====
app.include_router(UserController.router)
app.include_router(EmailController.router)
