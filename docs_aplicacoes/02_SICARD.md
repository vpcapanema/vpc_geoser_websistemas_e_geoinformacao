# SICARD

**Sistema Inteligente de Cadastro e Ranking de Demandas**

> Informação necessária, decisão rastreável.

---

## O problema

Toda instituição que executa orçamento precisa responder a uma pergunta desconfortável: **por que este projeto e não aquele?**

As demandas chegam por caminhos distintos — ofício de prefeitura, pleito de vereador, diagnóstico técnico interno, pressão de setor produtivo. Cada uma vem em um formato. Não há cadastro comum, não há critério explícito, e a priorização acaba se apoiando em quem tem mais acesso ao gestor.

Quando o questionamento vem — do controle interno, do Ministério Público, da imprensa, do próprio demandante preterido —, não há como reconstituir o raciocínio. A decisão foi tomada, mas não foi registrada.

## O que é

O SICARD organiza o ciclo completo de uma demanda pública, do protocolo à priorização homologada, tornando **explícitos os critérios, os pesos e as evidências** que sustentam cada posição no ranking.

Estrutura-se em três blocos:

**MOCAD — Módulo de Cadastro e Análise de Demandas.** Registro de planos, programas e projetos em um ciclo único: a mesma linha avança do cadastro à execução, sem migrar de sistema. Inclui criação, consulta, atualização, análise e aprovação, com a matriz de transições de status mantida no banco.

**MAD — Módulo de Apoio à Decisão.** Análise multicritério, matriz de comparação pareada, geoprocessamento e ranking.

**Transparência e Acompanhamento.** Camada pública com mapa das demandas publicadas, filtros e situação de cada registro.

## O ranking não é uma nota subjetiva

A hierarquização percorre quatro fases encadeadas:

1. **Elegibilidade territorial** — filtro por risco e restrição: o que não pode, sai antes de ser pontuado.
2. **Favorabilidade territorial** — o território responde se o projeto faz sentido ali.
3. **Ajuste fino por atributos** — características próprias do projeto refinam a posição.
4. **Síntese, ranking e homologação** — o resultado é fechado e assinado.

Cada rodada persiste o universo avaliado e os resultados em um **documento autocontido**. Meses depois é possível reabrir a rodada exatamente como ela foi.

## AHP com julgamento colaborativo

O módulo multicritério aplica o método de análise hierárquica com comparação pareada, cálculo de pesos e **verificação de consistência** — o sistema avisa quando o conjunto de julgamentos é internamente contraditório.

O diferencial está no modo colaborativo: em vez de um técnico definir os pesos sozinho, o sistema **emite convites com prazo e token de acesso público** para especialistas externos. Cada um responde seu formulário sem precisar de conta no sistema, e **cada matriz individual fica registrada com suas próprias métricas**.

O resultado deixa de ser "o critério do órgão" e passa a ser um julgamento coletivo documentado, com autoria e dispersão visíveis.

## Geoprocessamento embutido

Importação e catálogo de camadas, visualização vetorial e raster, operações individuais, jobs, funções e fluxos encadeados. O armazenamento separa fisicamente camadas importadas, processadas e homologadas — e **apenas os snapshots homologados formam a biblioteca oficial** consumida pelas fases de hierarquização.

Ou seja: ninguém prioriza projeto usando camada de teste.

## Abertura ao público

Qualquer pessoa, empresa ou instituição cadastra demanda pela área pública, sem barreira de acesso. O fluxo é declarado ao demandante: cadastro → análise técnica → disponibilização. Depois, acompanha a tramitação e consulta os resultados no mapa público.

A camada de transparência é honesta quanto ao próprio limite: o painel informa que exibe somente o que já foi liberado para consulta e que **a ausência de um registro não significa que ele não esteja em análise**.

## Integração, não duplicação

O SICARD **não mantém cadastro próprio de pessoas e instituições**. Ele se integra ao SIGMA-PLI, que é a autoridade de identidade do ecossistema, consumindo login, pessoas e instituições por API e banco, em leitura.

O dado tem um dono só. Os demais sistemas o consultam na origem.

## Controle de acesso por responsabilidade

Cinco perfis, derivados do usuário no sistema de identidade: **Visualizador** consulta; **Operador** cadastra, complementa e corrige; **Analista** avalia, aprova e disponibiliza; **Gestor** supervisiona o fluxo e valida resultados; **Administrador** cuida de usuários, permissões e configuração — sem herdar automaticamente as decisões de analista ou gestor.

Toda operação relevante fica na trilha de auditoria.

## Para quem

Órgãos que precisam distribuir recursos escassos entre demandas concorrentes e sustentar a escolha diante de controle externo: secretarias de infraestrutura, transporte e meio ambiente, autarquias de obras, fundos de investimento público, consórcios intermunicipais e programas com carteira de projetos.

## Base técnica

FastAPI e Python 3.11+ · PostgreSQL 17 com PostGIS 3.5 · frontend em HTML, CSS e JavaScript · integração por API REST com o sistema de identidade · esquemas separados por domínio (demandas, AHP, hierarquização, geo, geoprocessamento, auditoria) · Docker.

## Fundamento científico

**Método AHP de Saaty, implementado no servidor como fonte da verdade.** O vetor de prioridades é obtido pelo **autovetor principal aproximado por média geométrica normalizada** das linhas da matriz pareada:

```text
wᵢ = (∏ⱼ aᵢⱼ)^(1/n) / Σₖ (∏ⱼ aₖⱼ)^(1/n)
```

**Métricas de consistência completas**, na formulação canônica:

```text
λmax = (1/n) · Σᵢ [ (Σⱼ aᵢⱼ · wⱼ) / wᵢ ]
IC   = (λmax − n) / (n − 1)
RC   = IC / IA(n)
```

O índice aleatório **IA** é tabelado por dimensão da matriz, conforme os valores de referência de Saaty — 0,58 para n=3, 0,90 para n=4, 1,12 para n=5, até 1,49 para n=10.

A razão de consistência é o que distingue o AHP de uma ponderação arbitrária: ela mede se o conjunto de julgamentos é internamente transitivo. Julgar A > B, B > C e C > A produz RC alto, e o sistema recusa a matriz antes que ela vire ranking.

**Agregação de julgamentos individuais (AIJ).** No modo colaborativo, as matrizes dos especialistas são combinadas por **média geométrica em escala logarítmica** — o método correto para agregar razões, porque preserva a propriedade recíproca da matriz, o que a média aritmética destrói. O sistema aplica ainda um **filtro de RC máximo**: julgamentos individuais acima do limiar de inconsistência não contaminam o resultado do grupo.

Cada matriz individual permanece armazenada com suas próprias métricas. É possível auditar a dispersão entre especialistas, não apenas o consenso final.

**Análise multicritério em fases com normalização.** A hierarquização não aplica os pesos de uma vez. Percorre elegibilidade territorial (filtro binário por risco e restrição), favorabilidade territorial em dimensões de rede e de grade, ajuste por atributos do projeto e síntese. Os pesos entre dimensões são **normalizados para somar um**, com validação que rejeita conjunto de soma não positiva.

Separar filtro de pontuação é decisão metodológica relevante: restrição legal ou ambiental não deve ser compensável por pontuação alta em outro critério. O que não pode, sai antes.

**Geoprocessamento com rigor cartográfico.** O motor executa interseção geométrica, **estatística zonal**, buffer, dissolução, recorte e reprojeção, operando entre sistemas de referência oficiais brasileiros — SIRGAS 2000 nas zonas UTM 22S, 23S e 24S, Policônica, além dos sistemas geográficos e do de projeção web.

A escolha explícita entre método vetorial (interseção geométrica) e método raster (cobertura e estatística zonal) conforme a natureza do dado é o que separa um resultado geoespacial defensável de um número produzido por operação inadequada ao tipo de camada.

**Distinção entre camada de trabalho e camada oficial.** O armazenamento separa fisicamente camadas importadas, processadas e homologadas, e somente os snapshots homologados alimentam as fases de decisão. É controle de proveniência aplicado à análise espacial.

---

**Nota de enquadramento.** Sistema concebido e desenvolvido no contexto de um cliente específico. Este documento descreve a capacidade demonstrada; não constitui oferta de produto de prateleira nem autoriza revenda.

*Base de apuração: páginas públicas da aplicação (início, cadastro, transparência e documentação funcional), README e documentação do repositório.*
