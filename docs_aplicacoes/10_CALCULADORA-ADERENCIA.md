# Calculadora de Aderência Metodológica 2.0

**Avaliação de aderência metodológica de indicadores**

> O indicador é fácil de coletar. Mas ele mede o que você precisa medir?

---

## O problema

Todo plano, programa e política nasce com uma bateria de indicadores. E uma parte considerável deles é escolhida pelo motivo errado: porque o dado já existe, porque a série é longa, porque outro órgão usa, porque é fácil de coletar.

O resultado é um painel de monitoramento que acompanha com precisão coisas que não respondem à pergunta do plano. O erro só aparece anos depois, quando é preciso avaliar resultado e se descobre que nenhum indicador captura o fenômeno que importava.

A ferramenta parte de uma distinção explícita: **aderência não é popularidade do indicador nem facilidade de coleta**. É aderência ao fenômeno específico que o estudo pretende medir.

## O que é

Aplicação para cadastro, avaliação e consolidação da **aderência metodológica de indicadores**, com fluxo autônomo em múltiplas etapas e persistência local dos dados de trabalho.

## Como funciona

**Etapa 1 — Monte a ficha.** Cadastre os indicadores manualmente ou importe por CSV. Cada indicador precisa no mínimo de nome e descrição; área, unidade de medida e fonte enriquecem o relatório final. O importador trata aspas, vírgulas dentro de texto e comentários no topo do arquivo — detalhes que costumam quebrar importação de planilha real. Há template disponível para download.

**Etapa 2 — Avalie.** Atribua notas usando **rubricas descritivas**, com pesos por critério e **critérios eliminatórios**. Notas críticas exigem **justificativa obrigatória** — não é possível reprovar ou aprovar em silêncio.

**Etapa 3 — Consolide.** O sistema produz o **Índice de Aderência** em escala de 0 a 5, uma classificação padronizada, médias por critério e **análise de sensibilidade para cada indicador**, com exportação dos resultados.

## Por que a análise de sensibilidade importa

A sensibilidade responde à pergunta que derruba a maioria das avaliações multicritério: *o resultado muda se eu alterar um pouco os pesos?*

Se muda, a classificação é frágil e a decisão precisa de mais discussão. Se não muda, o ranking é robusto e pode ser defendido. Sem esse teste, uma avaliação ponderada é apenas uma opinião com aparência de cálculo.

## Rastreabilidade do julgamento

A aplicação registra quem avaliou e qual o objeto de estudo, mantém as justificativas das notas críticas e documenta a equação do índice com exemplo passo a passo. O relatório final não entrega só o número: entrega o caminho até ele.

## Para quem

Equipes de planejamento e monitoramento de planos e programas, áreas de avaliação de políticas públicas, escritórios de projetos, consultorias que estruturam sistemas de indicadores, e órgãos de controle que precisam verificar se o indicador contratado mede o que deveria medir.

## Base técnica

Aplicação web multipágina em HTML, CSS e JavaScript · persistência local no navegador, sem dependência de servidor · importação e exportação em CSV · fluxo autônomo, isolado de versões anteriores.

## Fundamento científico

**Índice de Aderência como soma ponderada normalizada:**

```text
IA = Σ (notaᵢ × pesoᵢ) / 100,   nota ∈ [0,5],   Σ peso = 100
```

**A rubrica de sete critérios é a contribuição metodológica central.** Ela ordena a avaliação por hierarquia epistemológica, não por conveniência operacional:

| Peso | Critério | O que interroga |
|---|---|---|
| 30 | Proximidade conceitual | O indicador mede o construto que o estudo definiu? |
| 20 | Mecanismo causal | Existe cadeia causal explícita entre o indicador e o fenômeno? |
| 15 | Validade empírica | Há evidência de que a relação se sustenta nos dados? |
| 10 | Especificidade | O indicador é sensível a este fenômeno e não a outros? |
| 10 | Sensibilidade | Ele varia quando o fenômeno varia? |
| 10 | Mensurabilidade | É possível medi-lo com confiabilidade? |
| 5 | Custo-benefício | Compensa o esforço de coleta? |

A distribuição dos pesos é uma tese: **65% da nota está nos três primeiros critérios** — validade conceitual, causal e empírica. Facilidade de coleta, o critério que na prática domina a escolha de indicadores no setor público, vale 5.

É a formalização do princípio declarado pela própria ferramenta: *aderência não é popularidade do indicador nem facilidade de coleta*.

**Critérios eliminatórios.** Proximidade conceitual e mecanismo causal têm **nota mínima 2**. Abaixo disso o indicador é reprovado independentemente do desempenho nos demais critérios — não há compensação.

Essa é a diferença entre um modelo compensatório e um modelo com restrição. Um indicador barato, disponível e fácil de medir, mas que não guarda relação causal com o fenômeno, não pode ser resgatado por pontuação alta em operacionalidade. A estrutura da rubrica impede exatamente o erro que ela foi criada para combater.

**Justificativa obrigatória em notas críticas.** O julgamento nos extremos exige texto. O relatório final carrega o argumento, não só o número — é o que torna a avaliação auditável por terceiro.

**Análise de sensibilidade.** Para cada indicador, o sistema testa a estabilidade do resultado frente a variações na ponderação. Um índice que muda de classificação com pequena alteração de pesos é frágil, e a fragilidade é reportada.

Sem esse teste, toda avaliação multicritério é uma opinião com aparência de cálculo. Com ele, é possível distinguir o resultado robusto do resultado que depende de uma escolha arbitrária de peso.

**Rubricas descritivas por nível de nota.** Cada ponto da escala tem descrição textual do que caracteriza aquele desempenho, reduzindo a variabilidade entre avaliadores — o problema clássico de confiabilidade interavaliadores em instrumentos de julgamento.

**Saída auditável.** Relatório exportável em JSON e CSV contendo notas, pesos, critérios eliminatórios aplicados, justificativas e a análise de sensibilidade. A avaliação inteira pode ser reconstituída e contestada.

---

**Nota de enquadramento.** Ferramenta metodológica desenvolvida no contexto do planejamento logístico estadual. Este documento descreve a capacidade demonstrada. Aplicação de acesso público.

*Base de apuração: interface pública da aplicação e código do repositório local.*
