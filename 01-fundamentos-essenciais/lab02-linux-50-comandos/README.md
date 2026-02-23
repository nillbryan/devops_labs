# Lab 02 — Linux (50 comandos) 🐧

Este lab é um **treino prático** para dominar comandos essenciais de Linux e gerar **evidências auditáveis** do seu estudo.

> **Objetivo:** aprender (e provar) que você sabe **navegar, manipular arquivos, buscar informação, inspecionar o sistema e diagnosticar problemas básicos** no Linux.

---

## ✅ Resultado esperado (o que você vai conseguir fazer no final)

Ao terminar, você consegue:
- Navegar e organizar pastas/arquivos com segurança.
- Manipular arquivos (copiar, mover, apagar com cuidado).
- Buscar informação em texto (grep, sort, head/tail).
- Entender permissões (chmod/chown) e evitar erros comuns.
- Inspecionar processos e recursos (CPU/RAM/disco).
- Fazer diagnósticos básicos de rede (ip/ss/curl/ping).
- Registrar evidências do estudo em `evidencias/`.

---

## 🧠 Regra de ouro (pra não se perder)

- **README.md** = instruções do que fazer (limpo, sem outputs).
- **evidencias/*.txt** = “provas” do que você rodou (saída real do terminal).

O comando `tee` é o que gera evidências:
- mostra na tela
- e salva no arquivo ao mesmo tempo

Exemplo simples:
```bash
ls -la | tee evidencias/exemplo.txt
