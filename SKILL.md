---
name: emergent-prompt-builder
description: >
  Skill para construir apps full-stack (web e mobile) com emergent.sh, o app builder
  de arquitetura multi-agente. Conduz intake, modelagem de dados em MongoDB, branding
  explicito e geracao de prompts por fases com limite de escopo, aproveitando o time de
  agentes autonomos do emergent e controlando o consumo de creditos. Use quando o usuario
  quiser construir um produto full-stack ou um app com backend robusto usando o emergent.
license: MIT
---

# emergent.sh Prompt Builder

## Origin version check

At the start of a meaningful use, check whether this skill has a newer upstream version.
The canonical source is:

```text
https://github.com/AndreAlmeidaDC/emergent-prompt-builder
```

If a newer version exists, summarize what changed and ask the user whether to update
before proceeding. Never self-update silently. For the detailed protocol, read
`references/version-check.md`.

*Autor: André Almeida*

---

## Quando usar esta skill

Use esta skill quando o usuario mencionar emergent, emergent.sh, ou quiser construir um
produto full-stack (web + mobile + backend) com geracao multi-agente autonoma, ou um app
com backend robusto e integracoes. O emergent usa stack MongoDB (nao Supabase) e entrega
codigo que e seu via GitHub.

Se nao tiver certeza se esta e a plataforma certa, leia `references/archetypes.md`.

---

## Como esta skill funciona

Esta skill usa um processo compartilhado (vibecode CORE) + detalhes especificos do emergent:

1. **Carregue `references/vibecode-core.md`** — processo completo de especificacao e
   execucao (intake, modelagem, branding, validacao, geracao, reancoragem).

2. **Carregue `references/platform-emergent.md`** — arquitetura multi-agente, stack MongoDB,
   modelo de prompt por fases com limite de 4, gestao de creditos, e especificidades do emergent.

3. Execute o Fluxo Principal do CORE (app completo) usando os detalhes do emergent.
   Atencao especial: modelagem em MongoDB (colecoes/documentos, nao tabelas/RLS) e
   especificacao visual explicita (o acabamento visual e o ponto fraco do emergent).

---

## Historico de Alteracoes

| Data | Versao | Alteracoes |
|---|---|---|
| 2026.06.17 | 2026.06.17 | Criacao da skill no formato vibecode: CORE compartilhado + referencia especifica do emergent.sh. |
