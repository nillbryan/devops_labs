# Lab 04 — .gitignore (Docker/Node)

## Objetivo
Aplicar um `.gitignore` profissional para projetos com Docker/Node, evitando versionar:
- dependências (`node_modules/`)
- builds (`dist/`, `build/`)
- logs (`*.log`)
- segredos (`.env`, `.env.*`)

## Por que isso é importante
- reduz ruído no `git status`
- evita commitar arquivos enormes e desnecessários
- protege credenciais/segredos (principalmente `.env`)
- deixa o repositório mais “enterprise-grade”

## Como validar
- `git status` **não** deve mostrar `node_modules/`, `.env`, `dist/`, `*.log`
- `git check-ignore -v <arquivo>` deve apontar qual regra do `.gitignore` está ignorando

## Evidências
Veja: `evidencias/01-validacao-gitignore.txt`
