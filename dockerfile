# Escolhe uma imagem base com Python 3.11
FROM python:3.11-slim

# Atualiza o sistema e instala dependências básicas
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Cria um diretório de trabalho
WORKDIR /app

# Copia os requirements (se houver)
# COPY requirements.txt .

# Instala pip atualizado
RUN python -m pip install --upgrade pip setuptools wheel

# Instala dependências do projeto (descomente se tiver requirements.txt)
# RUN pip install -r requirements.txt

# Comando padrão
CMD ["python", "--version"]
