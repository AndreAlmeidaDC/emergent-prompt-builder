# emergent-prompt-builder

Skill de IA para construir produtos full-stack no **emergent.sh** — web e mobile, com
backend de verdade — aproveitando o time de agentes autônomos da plataforma sem queimar
créditos à toa nem aceitar o acabamento visual genérico que ele entrega por padrão.

---

## O problema que esta skill resolve

O emergent.sh é diferente da maioria dos app builders: ele não responde prompt a prompt,
ele funciona como um time de engenharia autônomo. Cinco agentes especializados planejam a
arquitetura, desenham a interface, escrevem o código, conectam integrações e validam o
resultado antes de entregar. Isso é poderoso, mas muda completamente como você precisa
trabalhar com ele — e quem chega tratando o emergent como um chat de código comum tropeça
em três coisas.

Primeiro, créditos. O emergent é faminto de créditos, e até manter um app no ar consome
um valor recorrente. Sem disciplina, você gasta crédito gerando o que poderia ter
planejado de graça antes.

Segundo, o visual. O emergent é forte em lógica e fraco em acabamento visual: ele entrega
apps funcionais, mas se você não especificar cor, fonte e ícone de forma explícita, o
resultado sai genérico e desalinhado.

Terceiro, o modo de trabalho. O emergent rende quando você dá um objetivo bem
especificado e deixa o time executar em fases curtas — e trava em loops caros quando
recebe pedidos vagos ou amplos demais.

Esta skill resolve os três: faz todo o planejamento antes de você gastar o primeiro
crédito, força a especificação visual explícita, e estrutura o trabalho em fases curtas
com a disciplina que o emergent recompensa.

## Como a skill foi pensada

A skill parte de um princípio: **no emergent, você dirige um time, não um editor**. O
trabalho dela é te fazer chegar com um objetivo claro e um plano em fases, para o time de
agentes executar bem e barato.

### Explorando as forças do emergent

- **O emergent entrega apps funcionais ponta a ponta** (frontend, backend, banco, auth,
  deploy). A skill aproveita isso modelando tudo antes — dados, papéis, integrações — para
  o time de agentes ter um alvo completo já no primeiro prompt.
- **O emergent tem debugging autônomo.** A skill conta com isso, mas te orienta a revisar
  se a correção foi na direção certa, em vez de aceitar cegamente.
- **O emergent faz web e mobile no mesmo projeto** (Expo/React Native). A skill trata os
  dois no mesmo fluxo, sem precisar de uma ferramenta separada para cada um.
- **O código é seu** (GitHub, extensão VS Code). A skill recomenda conectar o GitHub desde
  o início, para você não ficar preso à plataforma nem aos créditos.

### Mitigando as fraquezas do emergent

- **Consumo agressivo de créditos.** Mitigado movendo todo o intake, modelagem e branding
  para fora do emergent (no seu chat de IA, de graça), e adotando a regra de pedir o plano
  de implementação antes de mandar executar.
- **Visual genérico.** Mitigado com um bloco de especificação visual explícito — cor,
  fonte e ícone nomeados — porque o agente não adivinha bem estética.
- **Loops em pedido vago.** Mitigado com a estrutura de fases curtas (no máximo quatro
  prompts atômicos por fase) e a regra das duas tentativas: se um bug não sai em duas
  tentativas, pare e reformule em vez de deixar o agente queimar crédito em loop.
- **Stack MongoDB que confunde quem vem de SQL.** Mitigada com modelagem no vocabulário
  certo (coleções e documentos, não tabelas e RLS) desde a fase de dados.

## O que a skill faz, passo a passo

**Intake.** Escopo, público, modelo de negócio, concorrentes, features do MVP, e perguntas
específicas do emergent: web/mobile/ambos, necessidade de deploy hospedado (custo de
créditos), integrações e intenção de exportar para o GitHub.

**Modelagem.** Modelo de dados em coleções MongoDB (não tabelas), papéis e permissões via
backend, fluxo de usuário.

**Branding.** Bloco de especificação visual detalhado — porque o acabamento visual do
emergent depende inteiramente do que você especifica.

**Brief inicial + fases.** Monta o prompt inicial com visão, stack, dados, auth e visual,
e estrutura o build em fases curtas, pedindo o plano de implementação antes de executar.

**Loop de feedback.** Prompts atômicos por fase, regra das duas tentativas para evitar
loops caros, e reancoragem quando o time de agentes diverge.

**Gestão de créditos.** Orienta quando planejar (de graça, no chat) e quando gastar
(geração no emergent), tratando cada build como um sprint.

## Como usar

1. Carregue esta skill no seu chat de IA (Claude, ChatGPT, etc.)
2. Responda o intake — com atenção a web/mobile, deploy e integrações
3. Conecte o GitHub no emergent para ter o código versionado desde o início
4. Cole o brief inicial e, a cada fase, peça o plano antes de mandar executar
5. Use a regra das duas tentativas para não desperdiçar créditos em loops

A skill gera os prompts; você faz a ponte de copiar e colar para o emergent. Ela não se
conecta ao emergent nem executa nada por você — é uma ferramenta de raciocínio e
especificação, não de automação.

## FAQ

**Por que o emergent gasta tanto crédito?**
Porque cada agente faz trabalho real (planejar, codar, testar, debugar) e manter um app no
ar custa por volta de 50 créditos/mês. A skill mitiga isso planejando fora da plataforma e
limitando o escopo de cada fase.

**Por que MongoDB e não Supabase?**
É a stack fixa do emergent (React/Node/FastAPI/MongoDB). A skill modela os dados em
coleções e documentos, não em tabelas e RLS — usar vocabulário SQL atrapalha.

**O emergent faz app mobile mesmo?**
Faz, com Expo/React Native e deploy nas lojas via EAS, sem precisar de Mac. Se você quer
**só** um app mobile indie e rápido, o a0.dev pode servir melhor; se quer mobile com
backend robusto ou web + mobile juntos, o emergent é a escolha.

**O código é meu ou fico preso na plataforma?**
É seu. O emergent dá o código via GitHub e tem extensão de VS Code. Diferente de
plataformas com lock-in, você pode exportar e seguir fora dela.

**O visual fica bom?**
A lógica fica sólida; o visual depende de você. O emergent é fraco em acabamento estético,
então a skill força a especificação explícita de cor, fonte e ícone para compensar.

**A skill se conecta ao emergent automaticamente?**
Não. Ela gera os prompts e você cola no emergent. Funciona em qualquer chat de IA.

**Preciso ativar acessibilidade?**
Não. Acessibilidade é opcional e fica desligada por padrão. Logo no início do fluxo a
skill pergunta se o app terá interface web usada por terceiros ou se precisa atender a
requisito de acessibilidade. Se for uso interno, protótipo ou app da própria equipe,
responda que não e siga sem nenhum peso extra. Se responder que sim, a skill passa a
tratar acessibilidade como requisito de toda a UI, com base em
`references/accessibility-web.md`.

## Estrutura do repositório

```
SKILL.md                          # Ponto de entrada: papel e como usar
references/
  vibecode-core.md                # Processo de engenharia (compartilhado na família)
  platform-emergent.md            # Multi-agente, MongoDB, fases, créditos, mobile vs a0.dev
  archetypes.md                   # Guia de escolha de plataforma
  version-check.md                # Protocolo de auto-atualização
  accessibility-web.md            # Acessibilidade web (opcional, ver gate na Fase 1)
templates/
  PRD.md                          # Template de requisitos de produto
  DATA_MODEL.md                   # Template de modelo de dados
  USER_FLOW.md                    # Template de fluxo de usuário
scripts/
  validate_skill.py               # Validação local da skill
```

## Por que existem 6 skills e não uma só

Essa pergunta é legítima — o processo de fundo (especificar antes de gerar, modelar
dados, iterar de forma atômica, reancorar quando a IA perde o contexto) é o mesmo em
todas as plataformas. Seria tentador fazer uma skill única que cobre tudo.

Não fizemos, por três razões:

**1. Contexto desperdiçado.** Uma skill única carregaria as particularidades de seis
plataformas em toda sessão, sendo que você só usa uma. A maior parte do que entrasse no
contexto seria ruído para a sua tarefa. Skills separadas carregam só o que importa para
a plataforma que você escolheu.

**2. As plataformas divergem mais do que parecem.** O v0 gera componentes, não apps.
O a0.dev fala de telas e navegação, não de páginas e rotas. O Base44 não te dá o código.
O emergent usa MongoDB e um time de agentes; os outros não. Espremer tudo num fluxo único
exigiria tantos "se for plataforma X, faça Y" que o resultado seria confuso e frágil.

**3. Evolução independente.** Cada plataforma muda no seu ritmo. Quando uma lança um
recurso novo, a skill dela é atualizada sem tocar nas outras cinco.

O que é genuinamente compartilhado (o processo de engenharia) vive em um único arquivo,
`references/vibecode-core.md`, idêntico em todas as skills. Assim evitamos duplicação no
que importa e mantemos independência onde importa.

## Família vibecode

| Skill | Plataforma | Melhor para |
|---|---|---|
| [lovable-prompt-builder](https://github.com/AndreAlmeidaDC/lovable-prompt-builder) | Lovable | App web full-stack com fluxo guiado passo a passo |
| [bolt-prompt-builder](https://github.com/AndreAlmeidaDC/bolt-prompt-builder) | bolt.new | App web full-stack com brief único e controle total |
| [v0-prompt-builder](https://github.com/AndreAlmeidaDC/v0-prompt-builder) | v0 (Vercel) | Componentes React/shadcn de alta qualidade |
| [a0-prompt-builder](https://github.com/AndreAlmeidaDC/a0-prompt-builder) | a0.dev | App mobile nativo iOS/Android |
| [base44-prompt-builder](https://github.com/AndreAlmeidaDC/base44-prompt-builder) | Base44 | Ferramenta interna / protótipo com backend incluído |
| **emergent-prompt-builder** (esta skill) | emergent.sh | Full-stack multi-agente (web + mobile), código seu |

## Licença

MIT — André Almeida
