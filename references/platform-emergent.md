# Platform Reference — emergent.sh

emergent.sh é um app builder full-stack com arquitetura multi-agente. Diferente da
maioria, ele funciona como um time de engenharia autônomo: agentes especializados
planejam a arquitetura, desenham a UI, estruturam o banco, conectam APIs, testam e
fazem deploy. Faz apps web e mobile (Expo/React Native), com código que é seu (GitHub).

> **Pré-requisito:** complete as Fases 1 a 4 do CORE antes de usar esta referência.
> O emergent usa o Fluxo Principal do CORE (app completo). Para o modelo de dados,
> atenção: a stack é MongoDB, não Supabase — o vocabulário de modelagem muda.

---

## A diferença central: arquitetura multi-agente

O emergent não é um gerador de código que responde prompt a prompt. São cinco agentes
coordenados (Architect, Designer, Developer, Integration, Product Manager), sendo o
Product Manager uma camada de QA que valida a saída contra os requisitos antes do deploy.

O que isso muda na prática para você:

- O **Architect Agent faz perguntas de esclarecimento** quando o pedido é ambíguo. Isso
  é bom, mas especificar bem desde o início economiza créditos e elimina ciclos de revisão.
- O emergent tem **debugging autônomo**: quando o código gerado tem erro, ele detecta,
  analisa a causa e aplica a correção sem esperar você. Você não precisa diagnosticar
  cada erro, mas precisa revisar se a correção foi na direção certa.
- O modo de prompt ideal é **"dê um objetivo bem especificado e deixe o time executar"**,
  não micro-gerenciar cada linha.

---

## Stack fixa: MongoDB, não Supabase (atenção na modelagem)

Esta é a divergência mais importante em relação a outras plataformas de app web. O
emergent usa:

- Frontend: React / Next.js
- Backend: Node.js / FastAPI
- **Banco: MongoDB** (orientado a documentos, não relacional)
- Mobile: Expo / React Native

**Impacto na Fase 2 (modelagem de dados) do CORE:**

Você modela em **coleções e documentos**, não em tabelas e linhas. Não há RLS (Row Level
Security) do Postgres — a segurança de acesso a dados é feita via autenticação e
verificação de papel (role) no backend, não via policies de banco.

```
Modelo de dados (MongoDB):
- Coleção: users
  { _id, email, passwordHash, name, role, createdAt }
- Coleção: projects
  { _id, ownerId (ref users), name, status, createdAt }
- Coleção: tasks
  { _id, projectId (ref projects), title, priority, dueDate, done }

Relações: por referência (ownerId, projectId apontam para _id de outra coleção).
Segurança: cada endpoint verifica auth + role antes de ler/escrever.
Validação: defina schema de validação por coleção (campos obrigatórios, tipos).
```

Não fale em "tabelas", "SQL", "migrations" ou "RLS" nos prompts do emergent — fale em
coleções, documentos, referências e validação de schema.

---

## Perguntas adicionais de intake (Fase 1 do CORE)

Após as perguntas genéricas do CORE, adicione:

12. O produto é **web, mobile, ou ambos**? (o emergent faz os dois no mesmo projeto)
13. Vai precisar de **deploy hospedado** desde já? (cada app hospedado custa ~50
    créditos/mês — é uma decisão de custo, não trivial)
14. Quais **integrações** externas? (Stripe, Google Sheets, Airtable, Slack, APIs via MCP)
15. Pretende **exportar o código para o GitHub** e evoluir fora da plataforma? (o emergent
    permite; vale planejar a estrutura pensando nisso)

---

## Output de Branding (Fase 3 do CORE — formato emergent)

O acabamento visual é o ponto fraco reconhecido do emergent: ele entrega lógica sólida,
mas o visual sai genérico se você não for explícito. Por isso o bloco de branding precisa
ser mais detalhado aqui do que em plataformas com forte viés visual.

```
ESPECIFICAÇÃO VISUAL — [Nome do Projeto]

Cores (seja explícito, o agente não adivinha bem):
  Primária:    #[hex]  — uso: [CTAs, links]
  Secundária:  #[hex]  — uso: [elementos de apoio]
  Fundo:       #[hex]
  Texto:       #[hex]
  Sidebar:     #[hex]  (ex: "dark sidebar com accent roxo")

Tipografia:
  Fonte de títulos: [nome exato]
  Fonte de corpo:   [nome exato]

Ícones: [biblioteca específica, ex: Lucide / Heroicons]
Estilo: [minimalista / corporativo / etc — com referências concretas]
Dark mode: [sim / não]

INSTRUÇÃO PARA O EMERGENT:
Aplique exatamente esta especificação visual. Não substitua cores, fontes ou ícones
por padrões genéricos. Mantenha consistência visual entre todas as telas.
```

---

## Estrutura de prompt do emergent (fases + limite de 4)

O emergent rende melhor com o modelo que a documentação dele recomenda, e que é
compatível com o CORE: **dividir em fases sequenciais e limitar cada fase a no máximo
4 prompts curtos, atômicos e testáveis.**

### Prompt inicial (a "visão + primeira fase")

```
# [Nome do Projeto] — Emergent Build

## Visão (end state)
[Descrição concreta do produto pronto. O que faz, para quem, resultado final.
Concreto, não aspiracional.]

## Plataforma
[Web / Mobile / Ambos]

## Stack (padrão emergent)
React/Next.js + Node.js/FastAPI + MongoDB. [Mobile: Expo/React Native, se aplicável.]

## Modelo de dados (coleções MongoDB)
[Coleções, campos, referências — do Fase 2]

## Autenticação e papéis
[email/senha, social login; papéis e o que cada um acessa]

## Especificação visual
[Bloco de branding da Fase 3]

## Integrações
[Stripe, Slack, etc — se aplicável]

## FASE 1 — [nome da fase] (máximo 4 prompts)
Primeiro: me dê um plano de implementação para esta fase.
Depois execute apenas o primeiro item. Aguardo verificar antes do próximo.

Instruções de comportamento:
- Trabalhe em fases. Não construa tudo de uma vez.
- Uma feature impactante por vez.
- Se um bug não for resolvido em 2 tentativas, pare e me peça orientação
  em vez de tentar indefinidamente (economia de créditos).
```

### Loop por fase

Para cada fase seguinte, peça primeiro o **plano de implementação**, depois execute item
a item, no máximo 4 por fase, verificando cada um antes de avançar.

---

## Gestão de créditos (específico e importante no emergent)

O emergent é reconhecidamente faminto de créditos, e o deploy ativo custa por volta de
50 créditos/mês por app. Trate cada build como um sprint:

- **Planeje antes de promptar.** Toda a Fase 1-4 do CORE (intake, modelagem, branding,
  validação) acontece no seu chat de IA, de graça, antes de gastar crédito no emergent.
- **Peça sempre o plano de implementação antes de executar.** "Me dê o plano, não execute
  ainda" custa pouco e evita execução na direção errada.
- **Regra das 2 tentativas.** Se o agente não resolve um bug em duas tentativas, pare,
  limpe o contexto, reformule ou intervenha manualmente. Não deixe auto-retry infinito
  queimando créditos.
- **Decida o deploy conscientemente.** Manter o app hospitado tem custo recorrente. Se é
  protótipo, considere não manter o deploy ativo entre sessões de demonstração.

---

## Mobile no emergent vs a0.dev

Os dois fazem mobile com Expo/React Native. A diferença para a sua escolha:

- Use o **emergent** se você quer um produto **full-stack** (web + mobile + backend
  robusto no mesmo projeto), ou um app mobile com backend e integrações complexas.
- Use o **a0.dev** se você quer **só um app mobile**, indie, rápido, focado em store, sem
  a camada full-stack.

Se o usuário só quer mobile e nada de web/backend pesado, considere indicar o a0.dev.

---

## Artefatos de Reancoragem (Fase 5.5 do CORE)

Quando o emergent divergir do plano, recole na sessão:
- A Visão (end state) e a fase atual
- O modelo de dados (coleções MongoDB)
- A especificação visual (se o problema for estético)
- O plano de implementação da fase em andamento
- A instrução das 2 tentativas

---

## Código é seu (ponto forte a aproveitar)

Diferente de plataformas com lock-in, o emergent dá o código via GitHub e tem extensão
de VS Code para puxar o projeto localmente, ajustar e devolver. Recomendações:

- Conecte o GitHub desde o início para ter o código versionado fora da plataforma.
- Para customização pesada ou produção, exporte e trabalhe parte no seu ambiente.
- Isso reduz o risco de depender só dos créditos e da disponibilidade da plataforma.

---

## Limitações e Gotchas do emergent

- **Créditos.** O maior ponto de atenção. Deploy ativo ~50 créditos/mês; o salto de plano
  Standard ($20) para Pro ($200) é grande. Planeje uso.
- **Visual genérico.** Lógica é forte, acabamento visual é fraco. Compense com especificação
  visual explícita e revisão estética.
- **Preview web de 30 min por sessão.** Inconveniente em sessões longas — planeje validar
  em janelas.
- **Loops em prompt ambíguo.** O debugging autônomo é bom, mas prompt mal especificado
  pode gerar loops. Especificar bem e usar a regra das 2 tentativas evita.
- **Código de produção precisa de revisão.** Escala, performance e segurança do código
  gerado devem ser revisadas antes de produção séria.
- **Suporte lento fora do tier alto.** Sistema de ticket; respostas não são imediatas em
  planos menores.
