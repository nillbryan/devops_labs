# Lab 03 — Dockerfile Multistage (Node.js)

## Objetivo
Criar uma imagem Docker **profissional** usando **multistage build** e comprovar:
- build de imagem (single-stage vs multistage)
- redução de tamanho da imagem
- execução do container e testes via `curl`
- evidências auditáveis (outputs em `evidencias/`)

## Estrutura
- `app/` → código Node + Dockerfiles (`Dockerfile` e `Dockerfile.single`)
- `evidencias/` → outputs do terminal (provas)

---

## Como rodar (passo a passo)

### 1) Build das imagens (comparação)
**O que faz:** cria duas imagens: uma “normal” (single-stage) e outra “multistage”.  
**Por que:** multistage reduz tamanho e remove “peso” desnecessário da imagem final.

```bash
cd 02-containers-com-docker/lab03-dockerfile-multistage-node/app
docker build -t node-app:single -f Dockerfile.single .
docker build -t node-app:multi  -f Dockerfile .
docker images | grep -E '^node-app'
