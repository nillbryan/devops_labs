# Lab 02 — Docker + FastAPI (Python)

## Objetivo
Construir e rodar uma API **FastAPI** dentro de um container Docker, validando:
- build de imagem via Dockerfile
- execução do container com porta mapeada
- testes via curl
- documentação automática (OpenAPI/Swagger)
- evidências auditáveis (logs e outputs)

## Estrutura
- `app/` → código + Dockerfile
- `evidencias/` → outputs do terminal (provas)

## Como rodar (quickstart)

### 1) Build da imagem
**O que faz:** transforma o `Dockerfile` em uma **imagem Docker** local.  
**Por que:** sem imagem, não existe container para rodar.

```bash
cd 02-containers-com-docker/lab02-fastapi-app/app
docker build -t fastapi-app:lab02 .
docker images | grep -E "^fastapi-app"
