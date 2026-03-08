# Lab 02 — Docker + FastAPI (Python)

## Objetivo
Construir e rodar uma API **FastAPI** dentro de um container Docker, validando:
- build de imagem via Dockerfile
- execução do container com porta mapeada
- testes via curl
- documentação automática (OpenAPI/Swagger)
- evidências auditáveis (logs e outputs)

## Estrutura do Lab
- `app/` → código da API + `Dockerfile` + `requirements.txt`
- `evidencias/` → arquivos `.txt` com outputs do terminal (prova do estudo)

---

## Pré-requisitos
1) Docker funcionando no WSL/Docker Desktop

   docker version
   docker info >/dev/null && echo "Docker OK" || echo "Docker NOK"

> Observação importante (WSL + Docker Desktop):
> `sudo systemctl status docker` pode falhar com “Unit docker.service could not be found.”
> Isso é normal porque o daemon está no Docker Desktop (não como service systemd dentro do Ubuntu).

---

## Como rodar (passo a passo)

### 1) Build da imagem
**O que faz:** transforma o `Dockerfile` em uma **imagem** local.  
**Por que:** container só nasce a partir de uma imagem.

   cd 02-containers-com-docker/lab02-fastapi-app/app
   docker build -t fastapi-app:lab02 .
   docker images | grep -E '^fastapi-app'

### 2) Subir o container
**O que faz:** cria e inicia o container em background (`-d`) e mapeia porta `8000:8000`.  
**Por que:** você acessa a API no host via `http://localhost:8000`.

   docker rm -f fastapi_lab02 >/dev/null 2>&1 || true
   docker run -d --name fastapi_lab02 -p 8000:8000 fastapi-app:lab02
   docker ps --filter "name=fastapi_lab02"

> Explicando o comando “limpeza preventiva”:
> - `docker rm -f fastapi_lab02` remove o container se existir
> - `>/dev/null 2>&1` esconde saída/erros (não polui o terminal)
> - `|| true` garante que o script continue mesmo se não existir container

### 3) Ver logs
**O que faz:** mostra a saída do Uvicorn/FastAPI.  
**Por que:** troubleshooting #1 é sempre olhar logs.

   docker logs --tail 50 fastapi_lab02

### 4) Testar endpoints (curl)
**O que faz:** chama endpoints HTTP e valida status/JSON.  
**Por que:** prova objetiva de que a API está respondendo.

   curl -i http://localhost:8000/
   echo
   curl -i http://localhost:8000/health
   echo

### 5) Documentação automática (FastAPI)
**O que faz:** FastAPI gera documentação viva.  
**Por que:** padrão profissional em APIs.

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
- OpenAPI JSON: `http://localhost:8000/openapi.json`

Teste pelo terminal:

   curl -s http://localhost:8000/openapi.json | head -n 40

> Dica: para abrir no browser, você **não digita** `http://...` no terminal.
> Você abre no navegador (Chrome/Edge):
> `http://localhost:8000/docs`

### 6) Cleanup
**O que faz:** para e remove o container.  
**Por que:** evita lixo rodando e libera recursos/porta.

   docker stop fastapi_lab02
   docker rm fastapi_lab02

---

## Checklist de conclusão
- [ ] `docker images` mostra `fastapi-app:lab02`
- [ ] `docker ps` mostra `fastapi_lab02` como `Up`
- [ ] `GET /` retorna JSON com mensagem
- [ ] `GET /health` retorna `{"status":"ok"}`
- [ ] `GET /openapi.json` retorna OpenAPI
- [ ] Evidências existem em `evidencias/` (00–03)
