# Análise de Sinistros — Infosiga SP

**Análise exploratória de sinistros de trânsito do Estado de São Paulo**

> 1,36 milhão de registros. A pergunta é o que eles dizem.

---

## O problema

A base oficial de sinistros de trânsito de um estado grande é um patrimônio informacional subutilizado. Ela existe, é pública, é atualizada — e quase ninguém consegue extrair dela uma leitura acionável.

O painel oficial responde consultas pontuais. Não responde por que a curva de óbitos se comporta assim, onde a fatalidade se concentra em relação à malha rodoviária, qual perfil demográfico está exposto a qual modal, ou como o padrão mudou ao longo de uma década.

## O que é

Análise exploratória completa da base oficial de sinistros de trânsito do Estado de São Paulo, integrada à malha rodoviária estadual, cobrindo o período de **2014 a 2026**.

## A escala

| Indicador | Volume |
|---|---|
| Sinistros registrados | 1.364.070 |
| Sinistros com vítima | 798.445 (58,5%) |
| Sinistros fatais | 58.200 (4,27%) |
| Óbitos | 62.029 |
| Feridos graves | 95.166 |
| Feridos leves | 817.271 |
| Pessoas envolvidas | 1.119.698 |
| Registros com geolocalização | 92,3% |
| Sinistros em rodovias | 16,6% |

## O que entrega

**Dashboard interativo** com os gráficos organizados em cinco categorias temáticas: visão geral, vítimas e demografia, séries temporais, análise geográfica e padrões.

**Análise geográfica** com visão tática por rodovia e por subtrecho sobre a malha rodoviária estadual completa — mapa navegável, ranking, série temporal e composição por tipo de evento. É aqui que a base sai da estatística agregada e vira instrumento de priorização de intervenção: qual subtrecho concentra fatalidade.

**Relatório executivo** consolidado, com principais achados, contextualização da fonte, ressalvas metodológicas e recomendações.

**Guia de acesso** com a lista de todos os gráficos e a descrição de cada análise.

## O que o torna confiável

A análise **declara os próprios limites** em vez de escondê-los:

- Os registros têm caráter **notificacional** — refletem o que foi notificado, não necessariamente o universo de ocorrências.
- Dados dos últimos 90 dias são **preliminares** e podem mudar.
- A geolocalização é derivada dos boletins e cobre **92,3%** do conjunto — o que sobra não é zero, é desconhecido.

Também explicita a natureza da fonte: sistema oficial de integração mantido pelo órgão de trânsito estadual com contribuição da agência reguladora de transporte, do departamento de estradas, das polícias civil, militar e rodoviária federal e da fundação estadual de estatística, consolidando três visões — sinistro, vítima e veículo.

Análise de segurança viária que omite ressalva metodológica produz política pública mal calibrada. Esta não omite.

## Para quem

Órgãos de trânsito e rodoviários, secretarias de segurança e mobilidade, concessionárias, observatórios de segurança viária, pesquisadores e equipes de planejamento de intervenções de engenharia de tráfego.

## Base técnica

Pipeline em Python com ETL e consolidação da base bruta, cruzamento espacial com a malha rodoviária e geração de dashboards · GeoPandas · Plotly para gráficos interativos · Leaflet para o mapa navegável · saída em HTML estático publicável.

## Fundamento científico

**Integração de três visões relacionais.** A base oficial consolida três perspectivas do mesmo evento — sinistro, vítima e veículo — em relação um-para-muitos. Analisá-las sem cuidado produz erro de contagem clássico: somar vítimas como se fossem sinistros, ou contar o mesmo evento tantas vezes quantos veículos envolvidos. O pipeline trata as três visões preservando a unidade de análise correta para cada indicador.

**Junção espacial com a malha rodoviária.** O cruzamento entre o ponto do sinistro e a geometria linear da malha estadual é o que permite sair da estatística agregada e chegar à **análise por rodovia e por subtrecho** — a escala em que a intervenção de engenharia efetivamente acontece. É operação de vizinhança espacial, não de coincidência exata, porque a coordenada do boletim raramente cai sobre o eixo da via.

**Declaração de cobertura da geocodificação.** A análise informa que **92,3%** dos registros possuem geolocalização. O complemento não é tratado como zero: é declarado como desconhecido. Análise espacial que ignora cobertura incompleta atribui ausência de sinistro a áreas que apenas não foram geocodificadas — e produz priorização invertida.

**Ressalvas metodológicas como parte do resultado.** O estudo declara:

- **Caráter notificacional** dos registros — a base reflete o que foi notificado, não o universo de ocorrências. Subnotificação diferencial entre regiões ou tipos de evento é fonte de viés conhecida em epidemiologia de trânsito.
- **Dados preliminares** nos últimos 90 dias, sujeitos a revisão. Séries recentes não devem ser lidas como tendência consolidada.
- **Proveniência multi-institucional** — órgão de trânsito, agência reguladora, departamento de estradas, três polícias e fundação de estatística —, o que implica heterogeneidade de critério de registro entre as fontes.

Declarar limite de validade não enfraquece a análise. É o que a torna utilizável para política pública, porque delimita quais conclusões o dado sustenta e quais não.

**Análise exploratória multidimensional.** O estudo percorre as dimensões que a literatura de segurança viária estabelece como determinantes: temporal (sazonalidade, dia, hora), demográfica (idade, sexo, condição da vítima), modal (tipo de veículo e de usuário) e geográfica. A separação entre **sinistro, sinistro com vítima e sinistro fatal** — 58,5% e 4,27% do total — é a estratificação por gravidade que sustenta qualquer priorização de intervenção.

**Pipeline reprodutível.** Processamento estruturado em etapas versionadas — ETL e consolidação, cruzamento espacial, geração de saída —, executável do dado bruto ao dashboard final. A análise pode ser reexecutada quando a base for atualizada, sem retrabalho manual.

---

**Nota de enquadramento.** Produto analítico desenvolvido sobre base de dados pública. Este documento descreve a capacidade demonstrada. Aplicação de acesso público.

*Base de apuração: portal público da aplicação e README do repositório.*
