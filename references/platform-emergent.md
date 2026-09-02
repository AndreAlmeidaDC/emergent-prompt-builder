# Platform Reference — Emergent

**Última verificação:** 2026-09-02, documentação oficial do Emergent.

Emergent oferece agentes principais selecionáveis, sub-agentes com contexto filtrado, preview, testes, GitHub, deployment, rollback/forking, MCP, custom agents e um Mobile Agent baseado em Expo. Disponibilidade, nomes, planos, custos e limites mudam; revalide antes de decidir.

Fontes oficiais principais:

- https://help.emergent.sh/first-app
- https://help.emergent.sh/context-limits
- https://help.emergent.sh/github-integration
- https://help.emergent.sh/prompting-basics
- https://help.emergent.sh/mcp-model-context-protocol
- https://help.emergent.sh/mobile-app-development
- https://help.emergent.sh/pre-deployment-health-check

## Escolha do agente

A documentação atual apresenta agentes com perfis distintos, como E1, E1.5, E2, Prototype e Mobile. Não codifique uma tabela eterna. Na data do uso:

1. confirme opções disponíveis na conta/projeto;
2. escolha pelo tipo de trabalho e risco;
3. use o agente mais simples que consiga sustentar o contrato;
4. registre por que foi escolhido;
5. troque somente com checkpoint, savepoint e impacto de contexto conhecido.

Heurística:

- **Prototype:** validar direção ou interface descartável;
- **E1:** desenvolvimento full-stack normal com testes;
- **E1.5:** sessão longa que exige continuidade;
- **E2:** arquitetura/bug difícil que justifica investigação mais intensa;
- **Mobile:** projeto Expo/React Native;
- **custom/pro mode:** fluxo especializado com contrato explícito.

Esses nomes são claims voláteis, não identidade permanente da skill.

## Contrato de autonomia

Antes de iniciar, declare:

- objetivo e fora de escopo;
- decisões que o agente pode tomar;
- ações que exigem aprovação;
- dados e credenciais permitidos;
- orçamento ou limite operacional;
- sensores obrigatórios;
- checkpoint/savepoint;
- stop conditions;
- escalation conditions;
- rollback.

Exemplo de stop condition:

> Pare quando duas iterações consecutivas não produzirem nova evidência diagnóstica, repetirem a mesma falha, exigirem ampliar escopo/credencial/custo ou contradisserem o contrato.

Isso substitui regras cegas como “duas tentativas” ou “quatro prompts”.

## Contexto, sub-agentes e forking

Sub-agentes recebem contexto filtrado; o agente principal continua responsável por coerência. Em projetos longos:

- mantenha brief, decisões e estado em arquivos/GitHub;
- salve em marcos verificáveis;
- faça fork quando exploração precisa divergir sem contaminar a linha estável;
- compare alternativas por critérios, não por entusiasmo do agente;
- reancore quando o contexto perder fatos, escopo ou decisões.

## Stack e arquitetura

Não presuma uma única stack para todos os modos. O Mobile Agent documenta stack fixa Expo/React Native + FastAPI + MongoDB; outros agentes e integrações podem produzir arquiteturas diferentes.

Em projeto existente, inspecione. Em greenfield, escolha a menor arquitetura que entrega valor. Defina banco, auth, APIs, filas, storage e observabilidade somente quando o comportamento exigir.

## GitHub e savepoints

GitHub é a fonte durável para trabalho relevante:

1. branch isolada;
2. checkpoint antes de mudança arriscada;
3. commits pequenos;
4. testes antes de merge;
5. PR para revisão;
6. rollback praticável.

Não deixe uma longa conversa ser a única memória do projeto.

## Integrações, MCP e Universal Key

MCP e integrações ampliam o alcance do agente. Para cada ferramenta, registre:

- servidor/provedor e owner;
- operações read/write;
- dados e escopos;
- secrets;
- limites de custo;
- confirmação humana;
- idempotência e rollback;
- logs/auditoria.

Nunca cole secret em texto de exemplo ou prompt. Use mecanismo seguro da plataforma e ambiente de teste.

## Mobile Agent

Quando o modo for Mobile:

- declare Expo/React Native desde o início;
- modele telas, navegação, safe areas, permissões e offline;
- conheça a stack fixa documentada;
- teste preview sem confundi-lo com build nativo;
- exporte/salve no GitHub;
- use EAS/dev builds e aparelhos para recursos nativos;
- TestFlight/Play internal testing antes da produção;
- OTA somente dentro dos limites do runtime;
- store submission separada e aprovada.

## Prompt inicial

```text
Antes de construir, confirme o agente atual e produza um plano.

Objetivo: [resultado]
Modo: [prototype/web/mobile/custom]
Estado: [novo/existente]
Escopo e fora de escopo: [itens]
Autonomia permitida: [decisões]
Aprovação exigida: [ações]
Stop/escalation conditions: [regras]
Verificação: [sensores]
Git checkpoint: [branch/savepoint]

Não implemente até apresentar fatos observados, riscos, plano e custo/impacto provável.
```

## Prompt de fase

```text
Execute somente [slice] do plano aprovado.

Preserve: [itens]
Arquivos/recursos permitidos: [lista]
Contrato: [comportamento]
Dados: [sintéticos/ambiente]
Sensores: [testes]
Stop conditions: [regras]

Não publique nem use credenciais/produção.
Ao terminar, mostre diff, evidência nova, resultado e próximo checkpoint.
```

## Verificação independente

O health check e os testes do agente são sensores, não prova absoluta. Para risco material:

- use uma segunda sessão/agente ou revisão humana;
- verifique requisitos e diff sem confiar no resumo do autor;
- rode testes determinísticos;
- teste auth, dados, pagamentos e integrações negativamente;
- valide fluxo real e rollback.

## Claims voláteis

Não grave preços, créditos, contexto, tiers, modelos ou prazos de suporte. Consulte documentação oficial no momento da decisão e identifique a data.
