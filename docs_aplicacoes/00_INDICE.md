# Aplicações — textos comerciais

**Data:** 06 de setembro de 2026
**Estado:** material para revisão. Não substitui as definições oficiais vigentes.

Um documento comercial por aplicação do ecossistema PLI, redigido a partir da exploração direta das aplicações em operação, de suas documentações públicas e dos repositórios de código.

## Sistemas maiores

| # | Aplicação | Tema | Problema que resolve |
|---|---|---|---|
| 01 | [SIGMA-PLI](01_SIGMA-PLI.md) | Governança do conhecimento técnico | Acervo técnico que se perde entre gestões |
| 02 | [SICARD](02_SICARD.md) | Decisão multicritério | Priorizar projetos sem critério defensável |
| 03 | [PLI Smart Router](03_PLI-SMART-ROUTER.md) | Roteirização com risco | Rota curta que atravessa área sob alerta |
| 04 | [PLI Reporta](04_PLI-REPORTA.md) | Ocorrências verificadas | Relato de campo sem confiabilidade operacional |
| 05 | [PLI-HazardTrack](05_PLI-HAZARDTRACK.md) | Risco climático extremo | Alerta que chega depois do bloqueio |
| 06 | [FAD-Stats 2.0](06_FAD-STATS.md) | Análise estatística e territorial | Bases oficiais que não se cruzam |

## Análises exploratórias

| # | Aplicação | Tema | Problema que resolve |
|---|---|---|---|
| 07 | [Análise de Sinistros — Infosiga SP](07_ACIDENTES-INFOSIGA.md) | Segurança viária estadual | 1,36 milhão de registros sem leitura acionável |
| 08 | [Painel de Sinistros — DER/SP](08_ACIDENTES-DER.md) | Segurança viária rodoviária | Estatística anual que não vira intervenção |
| 09 | [Densidade da Malha — SP](09_DENSIDADE-MALHA-SP.md) | Cobertura de infraestrutura | Investimento decidido por pleito, não por carência |

## Ferramentas analíticas e de produção

| # | Aplicação | Tema | Problema que resolve |
|---|---|---|---|
| 10 | [Calculadora de Aderência 2.0](10_CALCULADORA-ADERENCIA.md) | Qualidade de indicadores | Indicador escolhido por ser fácil, não por medir o certo |
| 11 | [AHP Tool Calculator](11_AHP-TOOL-CALCULATOR.md) | Priorização multicritério | Pesos definidos sem justificativa |
| 12 | [Formulário de Embarcadores](12_FORMULARIO-EMBARCADORES.md) | Levantamento logístico de campo | Pesquisa que se perde na transcrição |

---

## Como o ecossistema se articula

Não são doze aplicações isoladas. Há integração real e verificável entre elas:

- **SIGMA-PLI é a autoridade de identidade e cadastro institucional.** O SICARD se integra a ele para login, pessoas e instituições — não duplica cadastro, consulta na origem.
- **PLI-HazardTrack e PLI Reporta publicam feeds** de risco e de ocorrências verificadas.
- **PLI Smart Router consome esses feeds** para recalcular rotas, sem conhecer a origem interna do dado.
- **FAD-Stats e as análises exploratórias** aparecem no hub de ferramentas do SIGMA-PLI.

O princípio de arquitetura é o mesmo em toda parte: cada sistema mantém apenas o domínio que lhe pertence e consulta os demais na fonte.

---

## O método científico como diferencial

Cada documento traz uma seção **Fundamento científico**, extraída do código e da documentação metodológica das próprias aplicações. É o que distingue estes sistemas de software equivalente sem lastro técnico.

| Aplicação | Método aplicado |
|---|---|
| SIGMA-PLI | Modelo de metadados polimórfico; teoria de grafos aplicada à governança — PageRank, centralidade de intermediação, detecção de comunidades; proveniência com hash de integridade; padrões OGC |
| SICARD | AHP de Saaty com autovetor por média geométrica, λmax, IC, IA tabelado e RC; agregação de julgamentos individuais (AIJ) em escala logarítmica; multicritério em fases com filtro não compensatório; estatística zonal e interseção geométrica em SIRGAS 2000 |
| PLI Smart Router | Caminho de custo mínimo em grafo ponderado; penalização multiplicativa de aresta; agregação por máximo; buffer de segurança; overlay para cálculo de exposição por camada |
| PLI Reporta | Modelo de scoring com sinais ponderados; curva de saturação exponencial para confirmação; decaimento exponencial de persistência; forense de imagem por análise de nível de erro; agrupamento espaço-temporal |
| PLI-HazardTrack | Envoltória crítica de deflagração I = K·Ac⁻⁰·⁹; regionalização geotécnica com K calibrado; composição de janelas observada e prevista; matriz de composição RA × ICC; validação por retrodição |
| FAD-Stats | Assimetria e curtose com classificação de forma; IQR para atípicos; Pearson e Spearman; regressão de tendência; índice I de Moran e detecção de agrupamentos espaciais; seis métodos de quebra cartográfica |
| Infosiga SP | Tratamento de relação um-para-muitos entre três visões; junção espacial com malha; declaração de cobertura de geocodificação; controle de viés de subnotificação |
| Sinistros DER/SP | Estratificação por gravidade; análise de correlação e de risco; dado bruto publicado para reprodução independente |
| Densidade da Malha | Dupla normalização territorial e demográfica; análise multiescalar tratando o problema da unidade de área modificável; estratificação por atributo |
| Aderência 2.0 | Rubrica ponderada com 65% do peso em validade conceitual, causal e empírica; critérios eliminatórios não compensatórios; análise de sensibilidade; rubricas descritivas para confiabilidade interavaliadores |
| AHP Tool | Escala fundamental de Saaty; matriz recíproca; autovetor principal; razão de consistência contra índice aleatório tabelado |
| Embarcadores | Questionário estruturado com controle de efeito de entrevistador; validação na origem por base cadastral oficial; vocabulário controlado; matriz origem-destino para modelagem de transporte |

Três princípios metodológicos atravessam todas elas:

1. **Indisponibilidade não é zero.** HazardTrack marca `no_data`; Infosiga declara os 7,7% sem geocodificação; Smart Router informa a saúde dos serviços de origem.
2. **O resultado carrega o método.** Fonte, parâmetro, peso e limitação acompanham o número — em relatório exportável, em log de sincronização, em anexo de rastreabilidade.
3. **Restrição não é compensável por pontuação.** Tanto na hierarquização do SICARD quanto na rubrica da Aderência, o que reprova por critério eliminatório não é resgatado por desempenho alto em outro lugar.

---

## Enquadramento comercial

Conforme `MISSAO_VPC.md` e `AGENTS.md`, a oferta principal da VPC é **solução sob medida**, não catálogo de produtos prontos. A maioria destas aplicações foi concebida no contexto de um cliente específico e **não constitui produto disponível para revenda**. A redação em formato de produto, solicitada para este material, serve à comunicação da capacidade demonstrada.

Cada documento traz sua própria nota de enquadramento e a base de apuração usada.

## Limite desta apuração

A exploração foi feita pelas **superfícies públicas** das aplicações, pelas documentações e pelos repositórios de código. O acesso autenticado às áreas restritas **não foi realizado** — a execução do login com as credenciais fornecidas foi bloqueada pelo controle de segurança do ambiente. Funcionalidades internas de área restrita estão descritas a partir da documentação e do código, não de uso direto.

Nenhum preço, prazo, SLA, garantia de resultado ou condição comercial foi definido neste material.
