# FAD-Stats 2.0

**Ferramenta de Análise Dinamizada de Dados**

> As bases oficiais existem. O que não existe é o cruzamento entre elas.

---

## O problema

Os dados estatísticos oficiais do Brasil são públicos, gratuitos e abundantes. Produção agrícola por município, pecuária, aquicultura, extração vegetal, exportações por produto e por porto, vínculos formais de emprego por atividade econômica, transporte ferroviário de cargas.

E são, na prática, inacessíveis para quem precisa decidir.

Cada base tem seu portal, seu formato, sua nomenclatura, sua granularidade. Cruzar produção agrícola com exportação e com emprego formal exige um analista com Python, semanas de trabalho e conhecimento das chaves de compatibilidade entre classificações. O resultado costuma ser uma planilha que só o autor entende e que ninguém consegue atualizar no ano seguinte.

## O que é

A FAD-Stats é uma plataforma de análise dinamizada de dados estatísticos oficiais, concebida como sistema institucional de apoio à análise e plataforma técnica de inteligência territorial. Ela integra bases federais distintas e permite explorá-las, cruzá-las e visualizá-las em diferentes recortes territoriais e temporais — sem escrever uma linha de código.

## As bases integradas

| Fonte | Bases | Conteúdo |
|---|---|---|
| **IBGE** | PAM, PPM, PAQ, PEVS, POA | produção agrícola municipal, pecuária, aquicultura, extração vegetal e silvicultura, produção de origem animal |
| **SECEX** | Comex Stat | exportações e importações por produto, UF e município, com classificação SH/NCM |
| **MTE** | RAIS | vínculos empregatícios formais, detalhados por atividade econômica e ocupação, cobertura municipal |
| **ANTT** | ANTTFER, PNL2050 | transporte ferroviário de cargas e projeções logísticas de transporte |

Cinco pesquisas do IBGE, quatro fontes oficiais, **21 tipos de gráfico e 6 tipos de mapa**.

## A análise tem uma gramática

Toda consulta segue uma estrutura lógica obrigatória:

`Fonte → Pesquisa → Produto → Variável → Período → Território`

Primeiro o usuário define **o que analisar**; então o sistema **habilita automaticamente as visualizações compatíveis** — ou seja, decide *como mostrar* a partir do que foi pedido.

Isso elimina de saída a categoria de erro mais comum em ferramentas de BI genéricas: o gráfico tecnicamente possível e analiticamente sem sentido. Não se oferece mapa coroplético para série temporal de dez anos, nem linha do tempo para um único ano.

## Cinco perguntas, cinco formas

O usuário parte da pergunta, não do gráfico:

| Pergunta | Visualização habilitada |
|---|---|
| Como isto mudou ao longo dos anos? | linhas, múltiplos anos |
| Como se distribui no espaço? | mapa coroplético, um ano |
| Quem lidera? | barras horizontais, top N |
| Qual a participação de cada parte? | pizza ou treemap |
| Como se comparam lado a lado? | barras agrupadas, 1 a 3 anos |

E, para quem já sabe o que quer, o modo personalizado libera todas as opções.

## Análise cruzada: o diferencial

Além da análise individual sobre uma fonte, a plataforma executa **cruzamento entre bases distintas**, combinando dados de origens diferentes para revelar relações entre produção, comércio, emprego e logística.

O cruzamento é automático, usando **chaves de compatibilidade** entre as classificações — código de produto, classificação de atividade econômica, código municipal do IBGE e chaves espaciais por unidade federativa. É exatamente o trabalho manual que consumia semanas de analista.

Perguntas que a ferramenta responde diretamente:

- Evolução da produção de soja nos municípios de um estado ao longo de uma década
- Ranking dos estados que mais exportam determinada carne
- Relação entre exportações e emprego formal por região
- Série temporal comparando produção agrícola com volume exportado
- Relação entre transporte ferroviário de cargas, exportações e emprego formal por UF

## Cartografia de verdade

O módulo de mapa não é um mapa de enfeite. Oferece controle sobre **modo** (contínuo ou discreto), **número de classes** (3 a 9), **método de quebras** — quantil, intervalo igual, quebras naturais de Jenks, desvio padrão, intervalo geométrico, valores arredondados — e seis paletas, incluindo sequencial, divergente e perceptualmente uniforme.

São as escolhas que separam um mapa temático correto de um mapa que mente por classificação mal feita.

## Saída para trabalho real

Resultado exportável em **PNG, CSV, XLSX, PDF e JSON**, com resumo estatístico descritivo e módulo de estatística avançada acompanhando cada análise. O que sai da ferramenta entra no relatório, na planilha ou no próximo sistema.

## Recortes territoriais

Brasil inteiro, regiões, unidades federativas e municípios, com filtros encadeados — a seleção de UF condiciona a lista de municípios. Período pontual, comparativo entre anos escolhidos ou série temporal contínua.

## Para quem

Secretarias de planejamento, desenvolvimento econômico e agricultura; agências de fomento; equipes de estudos logísticos e de infraestrutura; consultorias que produzem diagnóstico territorial; e qualquer área técnica que hoje pede uma extração de dados e espera duas semanas por ela.

## Base técnica

FastAPI e Python · PostgreSQL · frontend em HTML, CSS e JavaScript sem etapa de build · catálogo espacial em GeoJSON · endpoints dedicados de gráfico, mapa, catálogo e cruzamento · controle de taxa de requisição e métricas · Docker.

## Fundamento científico

A FAD-Stats não devolve apenas gráfico. Cada análise vem acompanhada de um módulo estatístico que caracteriza a distribuição, testa relações e interpreta o resultado em texto.

**Estatística descritiva e forma da distribuição.** Medidas de posição e dispersão, quartis e percentis, **assimetria** e **curtose**, com classificação da forma — mesocúrtica, leptocúrtica ou platicúrtica. Não é ornamento: distribuição fortemente assimétrica invalida leitura por média, e a ferramenta sinaliza isso antes que alguém tire a conclusão errada.

**Detecção de valores atípicos** pelo critério do intervalo interquartil, com identificação nominal de quais territórios ou produtos são os discrepantes — o outlier é apontado, não apenas contado.

**Análise de concentração.** Curva de Pareto e participação do maior elemento no total, respondendo quanto do fenômeno se explica por poucas unidades. Em análise de produção e comércio exterior, concentração é frequentemente o achado principal.

**Correlação e tendência.** Coeficientes de **Pearson** (linear) e **Spearman** (por postos, robusto a não linearidade e a outliers) para as análises cruzadas, e **regressão linear simples** para extração de tendência em série temporal, com classificação do sentido — crescente, decrescente ou estável — e ajuste da reta devolvido junto com os dados.

A disponibilidade dos dois coeficientes importa: dados econômicos municipais raramente satisfazem os pressupostos de Pearson, e usar apenas ele produz correlação subestimada ou espúria.

**Autocorrelação espacial.** O módulo espacial calcula o **índice I de Moran** e identifica agrupamentos de valores altos e de valores baixos — *hot spots* e *cold spots*. A interpretação é devolvida em texto: se há clusters territoriais correlacionados ou se a distribuição é dispersa e sem padrão espacial.

Esta é a diferença entre um mapa e uma análise espacial. O mapa mostra onde os valores estão; o I de Moran responde se essa distribuição é estatisticamente diferente do acaso. Sem esse teste, qualquer mancha no mapa vira narrativa.

**Classificação cartográfica com método explícito.** Seis métodos de quebra disponíveis: **quantil**, **intervalo igual**, **quebras naturais de Jenks** (minimização da variância intraclasse), **desvio padrão**, **intervalo geométrico** e valores arredondados, com 3 a 9 classes e paletas sequencial, divergente e perceptualmente uniforme.

A escolha do método de classificação altera radicalmente a leitura de um mapa coroplético a partir dos mesmos dados. Expor esse controle ao usuário — em vez de esconder um padrão — é o que torna o mapa auditável.

**Compatibilização entre classificações oficiais.** O cruzamento entre bases distintas é feito por chaves de correspondência entre sistemas de classificação: nomenclatura de produto do comércio exterior, classificação nacional de atividade econômica, código municipal do instituto de estatística e chaves espaciais por unidade federativa.

Esse é o trabalho técnico que a ferramenta internaliza: cruzar produção agrícola com exportação e com emprego formal exige reconciliar três taxonomias que não foram desenhadas para conversar entre si.

**Gramática de análise como controle metodológico.** A sequência obrigatória fonte → pesquisa → produto → variável → período → território, com habilitação automática apenas das visualizações compatíveis, é um mecanismo de prevenção de erro analítico embutido na interface — impede a construção de gráficos tecnicamente possíveis e metodologicamente inválidos.

---

**Nota de enquadramento.** Sistema concebido e desenvolvido no contexto de um cliente específico. Este documento descreve a capacidade demonstrada; não constitui oferta de produto de prateleira nem autoriza revenda.

*Base de apuração: interface pública da aplicação, README e estrutura do repositório.*
