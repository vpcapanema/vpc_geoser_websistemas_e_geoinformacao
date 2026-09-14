# PLI Smart Router

**Roteamento rodoviário inteligente**

> A rota mais curta não é a melhor rota quando a estrada está sob alerta.

---

## O problema

Todo roteirizador responde à mesma pergunta: qual o caminho mais curto entre dois pontos? A resposta é calculada sobre uma base estática — a malha viária como ela é no mapa.

Só que a malha no mapa e a malha na terça-feira de manhã são coisas diferentes. Há trecho interditado por escorregamento, há alagamento, há área sob risco de fogo, há bloqueio que ninguém cadastrou ainda. O roteirizador não sabe de nada disso e manda o comboio direto para lá.

Para quem opera transporte de carga, atendimento emergencial, fiscalização ou logística de obra, a diferença entre "mais curto" e "transitável agora" é o que separa a operação do prejuízo.

## O que é

O Smart Router calcula rotas rodoviárias **considerando camadas de adversidade** sobrepostas ao território. Cada camada classifica o risco em categorias de severidade; conforme a categoria encontrada no caminho, o sistema propõe uma rota alternativa que contorna as áreas de maior risco.

## Duas rotas, lado a lado

**Rota Convencional** — o caminho mais curto, calculado sobre malha aberta. A análise convencional considera todos os níveis de risco encontrados, apenas não desvia deles.

**Rota Smart** — o caminho que desvia das adversidades presentes nas camadas ativas, com faixa de segurança em torno dos obstáculos.

As duas aparecem no mapa ao mesmo tempo. O operador vê o que está trocando: quanto tempo e quanto quilômetro custa evitar aquele trecho.

## O gatilho é configurável

O sistema não decide sozinho quando desviar. O operador define a partir de qual severidade o desvio automático é acionado:

- somente alerta máximo
- alerta crítico
- alerta
- atenção
- nunca automaticamente

Uma transportadora de carga geral e uma operação de transporte de produto perigoso não têm a mesma tolerância. O parâmetro acompanha a política de risco de cada operação.

## Camadas de adversidade

O catálogo é dinâmico e integra os sistemas de risco do ecossistema:

- **Risco a movimentos de massa** — risco geológico por unidade de análise
- **Risco a inundação** — risco hidrológico por unidade de análise
- **Risco a incêndios** — risco de fogo agregado por trecho rodoviário
- **Ocorrências verificadas em campo** — bloqueios, alagamentos, acidentes, obras e lentidão reportados e validados

As camadas de risco vêm do PLI-HazardTrack; as ocorrências, do PLI Reporta. Não são arquivos importados: são feeds consumidos com cache de curta duração e verificação de saúde dos serviços de origem.

## O que ele mede — e este é o ponto

Para **cada camada de adversidade ativa**, o sistema calcula ao longo de **toda a extensão da rota**:

- **tempo** exposto àquela camada
- **distância** exposta àquela camada
- **percentual de sobreposição** da rota com aquela camada

Não é um indicador agregado de "risco da viagem". É a decomposição por tipo de adversidade, trecho a trecho. O gestor sabe que 12% da rota atravessa área de risco de fogo e 3% atravessa unidade de análise em alerta geológico — e decide com esse número na mão.

O resultado aparece em tela e é **exportável em múltiplos formatos**, incluindo JSON com geometria e metadados e Shapefile compactado em WGS84, pronto para entrar em qualquer SIG.

## Entrada flexível

Origem e destino podem ser informados por **coordenadas**, **busca textual** — cidade, endereço ou CEP, com autocomplete — ou **clique direto no mapa**. A resolução de CEP e endereço usa serviços públicos de geocodificação.

## Interface de trabalho

Catálogo de camadas em árvore, no padrão de SIG desktop, com grupos colapsáveis, simbologia e contagem de feições. Sete mapas base disponíveis, de vetorial claro a imagem de satélite. Painel flutuante com o resumo da análise. Responsivo, pensado para uso em campo.

## Para quem

Operadores de transporte e logística, defesa civil, concessionárias e órgãos rodoviários, equipes de manutenção e conservação, fiscalização ambiental e sanitária, e qualquer operação cujo deslocamento atravesse território sujeito a evento climático extremo.

## Base técnica

Flask e Python 3.11+ · Leaflet · motor de roteamento sobre base cartográfica aberta · geocodificação por serviços públicos · integração por API com os sistemas de risco e de ocorrências · cache em memória com TTL configurável · health check dos serviços upstream · exportação em JSON e Shapefile · Docker.

## Fundamento científico

**Teoria dos grafos aplicada à malha viária.** A rede rodoviária é modelada como grafo dirigido e ponderado, no qual cada aresta carrega um custo — tempo ou distância. O cálculo de rota é um problema clássico de caminho de custo mínimo, resolvido sobre topologia derivada de base cartográfica aberta.

**Risco como modificação do custo, não como filtro binário.** A contribuição metodológica está aqui. O risco não elimina trechos: **penaliza arestas de forma multiplicativa**, preservando a escala original do custo:

```text
w' = w · (1 + α · P)
```

A escolha do multiplicativo sobre o aditivo tem consequência prática. Um corredor lento penalizado fica proporcionalmente mais lento, não absurdamente mais lento — o que evita que o algoritmo produza desvios desproporcionais e mantém o resultado explicável ao operador em linguagem direta.

A remoção efetiva da aresta do grafo é reservada a bloqueio total de alta confiança, tratado fora do modelo contínuo.

**Agregação por máximo, não por soma.** Quando múltiplos incidentes afetam a mesma aresta, prevalece o de maior prioridade. A justificativa é física antes de ser computacional: o trecho tem o pior problema reportado, não a média deles. E é robusta contra inflação artificial por relatos repetidos no mesmo ponto.

**Buffer de segurança como operação espacial.** O desvio não contorna o ponto do incidente, mas uma **zona de influência gerada por buffer** em torno da feição de risco. É a diferença entre passar ao lado de uma área instável e passar longe dela.

**Análise de sobreposição espacial rota-camada.** Para cada camada de adversidade, o sistema executa **overlay** entre a geometria linear da rota e as feições de risco, calculando o comprimento da interseção. Daí derivam os três indicadores por camada:

```text
distância exposta = Σ comprimento(rota ∩ feições de risco da camada)
% sobreposição    = distância exposta / comprimento total da rota
tempo exposto     = distância exposta / velocidade do trecho
```

A decisão de **não agregar as camadas em um índice único de risco** é metodológica: movimento de massa, inundação e incêndio são processos com física, temporalidade e resposta operacional distintas. Somá-los em um número produziria um indicador sem significado físico e sem utilidade para decisão. O gestor recebe o vetor, não o escalar.

**Limiar de acionamento parametrizável.** O gatilho de recálculo automático é exposto como parâmetro por categoria de severidade. Isso transfere a definição de tolerância ao risco para a política da organização, em vez de embuti-la como constante no código — princípio de separação entre motor de cálculo e critério de decisão.

**Classificação de severidade herdada da fonte.** O roteirizador não reclassifica risco: consome as categorias já classificadas pelos sistemas de origem, que aplicam suas próprias metodologias. Cada sistema mantém a autoridade sobre o próprio domínio metodológico.

**Cache com tempo de vida diferenciado por natureza do fenômeno.** Camadas de risco geofísico e ocorrências de campo têm janelas de validade distintas, calibradas pela velocidade com que cada fenômeno muda.

---

**Nota de enquadramento.** Sistema concebido e desenvolvido no contexto de um cliente específico. Este documento descreve a capacidade demonstrada; não constitui oferta de produto de prateleira nem autoriza revenda.

*Base de apuração: interface pública da aplicação, README e documentação do repositório, e descrição funcional fornecida pelo responsável técnico.*
