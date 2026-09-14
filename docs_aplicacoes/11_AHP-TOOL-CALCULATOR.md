# AHP Tool Calculator

**Análise hierárquica de processos para decisão multicritério**

> Priorizar é comparar. O método só exige que você compare de dois em dois.

---

## O problema

Escolher entre dez alternativas usando seis critérios é uma tarefa que a intuição humana não executa bem. A mente compara duas coisas com competência razoável; dez coisas em seis dimensões, não.

Na ausência de método, a decisão colegiada colapsa no critério de quem fala mais, ou numa planilha de pesos definidos sem justificativa — "qualidade vale 30%" — que ninguém consegue defender depois.

## O que é

Sistema web completo de análise de decisão multicritério pelo método de análise hierárquica de processos (AHP), formulado por Thomas Saaty. O método resolve o problema decompondo a decisão em **comparações par a par**, que a mente humana executa com confiabilidade, e derivando dali os pesos de todos os critérios simultaneamente.

## Processo guiado em cinco etapas

1. **Definição** do número de critérios (de 1 a 20)
2. **Nomeação** dos critérios
3. **Escolha do método de comparação** — matriz direta ou formulário
4. **Comparações pareadas** usando a escala de Saaty
5. **Resultados** com métricas completas

## Dois modos de comparação

**Matriz direta** — tabela completa com células editáveis, para quem já domina o método e quer velocidade. O sistema calcula automaticamente os valores recíprocos: preencher um lado da diagonal basta.

**Formulário** — comparações par a par apresentadas em lista, uma de cada vez, para quem está julgando pela primeira vez ou para colher julgamento de especialista não familiarizado com a notação matricial.

## Importação de matriz pronta

É possível **carregar matrizes pré-preenchidas** em CSV ou JSON, com validação automática de consistência, pulando direto para os resultados. Arquivos de exemplo acompanham a ferramenta.

O recurso atende ao caso real mais comum: a matriz foi construída em reunião, num quadro branco ou numa planilha, e precisa ser processada e verificada sem retrabalho de digitação guiada.

## Consistência: o que separa AHP de média ponderada

O valor do método está na **razão de consistência**. Se você julgou que A é mais importante que B, B mais que C, e depois que C é mais importante que A, o conjunto é contraditório — e o sistema mostra isso, com número.

Uma média ponderada aceita qualquer peso sem questionar. O AHP submete o julgamento a um teste interno e informa quando ele precisa ser revisto antes de virar decisão.

## Para quem

Comitês de priorização de projetos, comissões de licitação e julgamento técnico, equipes de planejamento que precisam ordenar carteira, avaliação de alternativas de projeto de engenharia, seleção de fornecedores e qualquer decisão colegiada que precise sobreviver a questionamento posterior.

## Base técnica

Aplicação web com interface guiada · implementação da escala de Saaty com cálculo de recíprocos, autovetor de pesos e razão de consistência · importação e exportação em CSV e JSON · padrão visual integrado ao ecossistema · assets locais, sem dependência externa.

## Fundamento científico

**Método de Saaty.** O AHP resolve um problema cognitivo real: a mente humana compara duas alternativas com confiabilidade razoável, mas não ordena dez alternativas em seis dimensões simultaneamente. O método decompõe a decisão em julgamentos pareados e reconstrói dali o vetor de prioridades global.

**Escala fundamental.** As comparações usam a escala de 1 a 9 de Saaty — de igual importância a importância extrema — com valores intermediários. A matriz é **recíproca por construção**: se A vale 5 em relação a B, B vale 1/5 em relação a A. O sistema calcula os recíprocos automaticamente, e por isso preencher metade da matriz basta.

**Vetor de prioridades.** Os pesos são obtidos pelo **autovetor principal** da matriz de comparações. A ferramenta usa a aproximação por média geométrica normalizada das linhas:

```text
wᵢ = (∏ⱼ aᵢⱼ)^(1/n) / Σₖ (∏ⱼ aₖⱼ)^(1/n)
```

A média geométrica é a operação correta para agregar razões — a média aritmética destruiria a propriedade recíproca da matriz.

**Verificação de consistência.** É o que distingue o AHP de uma ponderação arbitrária:

```text
λmax = (1/n) · Σᵢ [ (Σⱼ aᵢⱼ · wⱼ) / wᵢ ]
IC   = (λmax − n) / (n − 1)
RC   = IC / IA(n)
```

O **índice de consistência** mede o afastamento da matriz em relação à consistência perfeita, na qual λmax = n. A **razão de consistência** normaliza esse desvio pelo índice aleatório — o valor esperado de IC para matrizes preenchidas ao acaso, tabelado por dimensão.

A convenção da literatura é aceitar RC ≤ 0,10: até 10% de inconsistência em relação ao acaso. Acima disso, os julgamentos são internamente contraditórios e devem ser revistos antes de virar decisão.

**Por que a consistência importa.** Se o avaliador julgou que A é mais importante que B, que B é mais importante que C, e depois que C é mais importante que A, há violação de transitividade. Uma planilha de média ponderada aceita isso em silêncio e produz um ranking. O AHP mede a contradição e a devolve ao avaliador com número.

**Validação na importação.** Matrizes carregadas de arquivo externo passam por verificação automática de consistência antes de gerar resultado — o atalho não desliga o controle metodológico.

---

**Nota de enquadramento.** Ferramenta metodológica de escopo geral, aplicável fora do contexto em que foi desenvolvida. Aplicação de acesso público.

*Base de apuração: README do repositório e interface pública da aplicação.*
