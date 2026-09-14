# Painel Analítico de Sinistros — DER/SP

**Análise exploratória de acidentes nas rodovias estaduais**

> Três anos, quase 40 mil acidentes, uma pergunta: onde intervir primeiro?

---

## O problema

Um departamento de estradas registra acidente por obrigação. O registro vira estatística, a estatística vira relatório anual, e o relatório anual raramente muda uma decisão de engenharia.

Entre o dado bruto e a decisão de onde instalar defensa, refazer sinalização ou revisar geometria de curva, falta a camada analítica: a que compara rodovias entre si, mostra a evolução temporal, cruza gravidade com localização e aponta padrão.

## O que é

Análise exploratória completa dos acidentes registrados nas rodovias estaduais sob jurisdição do departamento de estradas, com dados consolidados de **2023, 2024 e 2025**.

## A escala

| Indicador | Volume |
|---|---|
| Total de acidentes | 39.578 |
| Total de vítimas | 34.324 |
| Anos analisados | 3 |
| Gráficos interativos | 29 |

**Evolução no período:**

| Ano | Acidentes | Vítimas | Óbitos |
|---|---|---|---|
| 2023 | 14.389 | 13.076 | 744 |
| 2024 | 13.882 | 13.426 | 769 |
| 2025 | 11.307 | 7.822 | 552 |

## O que entrega

**Dashboard interativo** com 29 gráficos organizados em seis categorias temáticas: visão geral e estatísticas, análise de vítimas, séries temporais, análise geográfica, padrões e correlações, e análise de risco.

**Dashboard compacto**, versão em grade com layout em abas e gráficos lado a lado, para leitura rápida e uso em apresentação.

**Relatório executivo** com análises, achados e recomendações estratégicas.

**Guia de acesso** com a lista completa dos gráficos e a descrição de cada análise.

**Downloads** em formato aberto: relatório detalhado, resumo final e a base completa em CSV — o usuário leva o dado consigo e faz sua própria análise.

## Por que é útil

O recorte por rodovia e por período é o que transforma volume em prioridade. Comparar trecho com trecho, ano com ano e gravidade com localização é o que sustenta a fila de intervenção de engenharia de segurança viária.

A categoria de **análise de risco** é a que fecha o ciclo: não descreve o que aconteceu, sinaliza onde a probabilidade está concentrada.

## Para quem

Departamentos de estradas de rodagem, concessionárias, órgãos de trânsito, equipes de engenharia de tráfego e segurança viária, e áreas de planejamento de investimento em infraestrutura rodoviária.

## Base técnica

Pipeline analítico em Python · gráficos interativos · saída em HTML estático publicável, sem dependência de servidor de aplicação · exportação em CSV e TXT.

## Fundamento científico

**Estratificação por gravidade.** A análise separa acidente, vítima e óbito como grandezas distintas, e não como escalas do mesmo número. A razão é metodológica: a distribuição espacial dos acidentes e a dos óbitos **não coincidem**. Trecho urbano concentra ocorrência; trecho de alta velocidade concentra letalidade. Priorizar intervenção pela contagem bruta de acidentes desloca recurso para onde há mais registro, não para onde há mais morte.

Os três anos analisados evidenciam por que a estratificação importa: entre 2023 e 2024 os acidentes caíram e os óbitos subiram. Um indicador único teria escondido a inversão.

**Análise de correlação e padrões.** Uma das seis categorias temáticas é dedicada a **padrões e correlações**, buscando associação entre variáveis — condições, período, tipo de via, perfil de envolvido. É a etapa que transforma descrição em hipótese causal testável, insumo do diagnóstico de engenharia.

**Análise de risco.** A categoria de risco não descreve o passado: sinaliza concentração de probabilidade. É a diferença entre relatório estatístico e instrumento de priorização — responde onde intervir, não apenas o que aconteceu.

**Série temporal em janela curta com ressalva implícita.** Três anos consecutivos permitem observar direção, mas não isolar tendência de flutuação aleatória. A apresentação ano a ano, sem extrapolação, é a leitura correta para essa extensão de série.

**Análise geográfica por recorte de rodovia e período.** O cruzamento entre localização e janela temporal é o que permite comparar trechos entre si e o mesmo trecho ao longo do tempo — condição para avaliar se uma intervenção já executada produziu efeito.

**Reprodutibilidade e dado aberto.** Além dos dashboards, o estudo disponibiliza a **base completa em CSV** e os relatórios em texto. Qualquer terceiro pode refazer a análise, contestar o recorte ou aplicar outro método sobre os mesmos dados — condição elementar de verificabilidade que raramente acompanha relatório de segurança viária.

**Saída em formato aberto e autocontido.** Os produtos são HTML estático com gráficos interativos, sem dependência de servidor de aplicação ou licença de plataforma de BI. O relatório continua funcionando daqui a cinco anos, em qualquer navegador, sem contrato de manutenção — princípio de portabilidade aplicado ao produto analítico.

---

**Nota de enquadramento.** Produto analítico desenvolvido sobre base de dados de órgão público. Este documento descreve a capacidade demonstrada. Aplicação de acesso público.

*Base de apuração: portal público da aplicação.*
