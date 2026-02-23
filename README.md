# DevOps Labs — Nill Bryan

Repositório de **estudos práticos (hands-on)** em DevOps/Cloud/SRE, com foco em:
- consolidar fundamentos (Linux, Git, redes, containers, CI/CD),
- gerar **evidências auditáveis** (prints/logs/artefatos),
- construir um **portfólio técnico** para entrevistas e evolução contínua.

---

## ✅ Como navegar (melhor dos dois mundos)

Este repo combina duas formas de organização:

### 1) Estrutura física por **módulos do curso**
- Pastas: `01-fundamentos-essenciais/`, `02-...`, etc.
- Índice oficial: **MODULOS.md**

➡️ Use quando você quiser estudar **em ordem** (como uma trilha do curso).

### 2) Índice lógico por **trilhas (assuntos)**
- Índice por tema: **TRILHAS.md**
- Temas típicos: Git, Linux, Docker, Kubernetes, CI/CD…

➡️ Use quando você quiser achar rapidamente “tudo de Linux”, por exemplo.

📌 Comece por:
- `MODULOS.md` (ordem do curso)
- `TRILHAS.md` (ordem por assunto)

---

## 📦 Padrão de um Lab

Cada lab segue este formato:

- `README.md` → objetivo, roteiro e checklist
- `evidencias/` → outputs, prints e artefatos (provas do estudo)

Sugestão de nomes em `evidencias/`:
- `01-comandos.txt`
- `02-output-ps-top.txt`
- `print-01-...png`

---

## 🧭 Roadmap (resumo)

### 01 — Fundamentos Essenciais
- Lab 01 — Git Essencial ✅
- Lab 02 — Linux (50 comandos) ✅

### Próximos (planejado)
- Docker
- Kubernetes
- CI/CD
- IaC (Terraform)
- Observability / Logging

---

## 🔒 Segurança (regras simples)
- Nunca commitar credenciais, tokens, chaves e `.env` com segredo.
- Se vazar algo: revogar/rotacionar imediatamente.
